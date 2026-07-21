## Let LLMs Generate A2UI

For the LLM-generates-UI pattern (the default introduced in 4.2), hand-coding A2UI JSON is tedious. Use the official a2ui-agent-sdk ( pip install a2ui-agent-sdk ): the A2uiSchemaManager builds a system prompt that already embeds the catalog schema and worked examples, the catalog ships its own JSON-Schema validator, and the same SDK provides a parser for the &lt;a2ui-json&gt; blocks the agent emits. Then validate and retry on schema errors.

```
Python # pip install a2ui-agent-sdk google-adk import asyncio, json import jsonschema from a2ui.schema.manager import A2uiSchemaManager from a2ui.basic_catalog.provider import BasicCatalog from a2ui.schema.constants import VERSION_0_9 from a2ui.parser.parser import parse_response from google.adk.agents import LlmAgent from google.adk.models import Gemini from google.adk.runners import InMemoryRunner from google.genai import types # 1. The SDK loads the catalog, builds the validator, and renders a complete #    system prompt with the schema and worked examples baked in. schema_manager = A2uiSchemaManager( version=VERSION_0_9, catalogs=[BasicCatalog.get_config(version=VERSION_0_9)], ) catalog = schema_manager.get_selected_catalog() Continues next page...
```

```
agent = LlmAgent( model=Gemini(model="gemini-flash-latest"), name="ui_agent", instruction=schema_manager.generate_system_prompt( role_description="You generate interactive UIs as A2UI v0.9 messages.", ui_description="Use Cards, Lists, ChoicePickers, and Buttons to present data.", include_schema=True, include_examples=True, ), ) # 2. Run the agent. It emits text containing one or more <a2ui-json>...</a2ui-json> #    blocks; parse_response() extracts the parsed JSON. Validate, then retry on errors. async def create_ui(intent: str, data: dict, max_retries: int = 3) -> list: runner = InMemoryRunner(agent=agent, app_name="ui_demo") session = await runner.session_service.create_session( app_name="ui_demo", user_id="u", state={"expression": "{expression}"},  # escapes the SDK's templating placeholder ) query = f"{intent}\n\nData: {json.dumps(data)}" last_error = None for _ in range(max_retries + 1): chunks = [] msg = types.Content(role="user", parts=[types.Part(text=query)]) async for ev in runner.run_async(user_id="u", session_id=session.id, new_message=msg): if ev.content and ev.content.parts: chunks.extend(p.text for p in ev.content.parts if p.text) blocks = [rp.a2ui_json for rp in parse_response("".join(chunks)) if rp.a2ui_json] try: for b in blocks: for m in (b if isinstance(b, list) else [b]): catalog.validator.validate(m) return blocks except jsonschema.ValidationError as e: Continues next page...
```

```
last_error = e path = "/".join(str(p) for p in e.absolute_path) query = ( f"Your previous response failed schema validation at {path}: " f"{e.message[:200]}\nFix this and retry: {intent}\nData: {json.dumps(data)}" ) raise ValueError(f"Schema validation failed after {max_retries} retries: {last_error}")
```

Snippet 6: A2uiSchemaManager implementation

In production, wrap create\_ui() in try/except and fall back to a text response on schema-validation failure. LLM output is stochastic, and the renderer should never see a malformed payload.
