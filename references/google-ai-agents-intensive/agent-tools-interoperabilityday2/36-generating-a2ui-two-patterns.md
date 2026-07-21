## Generating A2UI: Two Patterns

There are two ways to produce A2UI in practice, and the choice is mostly about where the layout decision lives.

The default is to let the LLM emit A2UI directly: the model owns the layout, adapts it to user intent, and the same agent handles "compare these regions" and "show me trends" with different interfaces. Production code for this pattern uses the official a2ui-agent-sdk and lives in 4.4.

The specialization is to have a tool return a fixed A2UI structure: one tool call, no LLM tokens spent on UI generation, fully predictable output. This is the right call when the layout is deterministic from inputs: every region's sales dashboard looks the same, every booking form has the same fields. Effectively, the tool is a server-side template.

A clean tool-as-template tool does two things in its body: build the A2UI structure with data bindings (path references, not f-string interpolation) and return it. The framework's A2uiPartConverter (from a2ui-agent-sdk ) intercepts the tool's response and routes it to the client as an A2UI part, so the tool itself stays a plain Python function:

```
Python from google.adk.agents import LlmAgent from google.adk.models import Gemini def   get_sales_dashboard(region: str) -> dict: """Build a data-bound sales dashboard for `region`.""" data = fetch_sales(region) return { "version": "v0.9", "updateComponents": { "surfaceId": "sales", "components": [ {"id": "root", "component": "Column", "children": ["title", "total", "drill"]}, {"id": "title", "component": "Text", "text": {"path": "/title"}, "variant": "h1"}, Continues next page.. .
```

```
{"id": "total", "component": "Text", "text", {"path": "/total"}}, {"id": "drill", "component": "Button", "child": "drill-label", "action": {"event": {"name": "expand_details"}}}, {"id": "drill-label", "component": "Text", "text": "Drill Down"}, ], }, } agent = LlmAgent( name="sales_agent", model=Gemini(model="gemini-flash-latest"), tools=[get_sales_dashboard], ) # Wire the converter at executor setup so this tool's response becomes an A2UI part: #   from a2ui.adk.send_a2ui_to_client_toolset import A2uiPartConverter #   A2aAgentExecutorConfig(event_converter=A2uiPartConverter(catalog, bypass_tool_check=True))
```

Snippet 5: LLM-generates-UI pattern

Data values flow through a parallel updateDataModel message that resolves the {path: "/title"} references, so clients can re-render on data updates without re-sending the structure. The LLM only sees a structured tool response (not the rendered UI) so its context stays focused on what to do next, not on the UI it just built.
