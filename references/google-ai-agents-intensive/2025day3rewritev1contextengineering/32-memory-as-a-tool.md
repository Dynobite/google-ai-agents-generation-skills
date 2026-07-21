## Memory-as-a-Tool

A more sophisticated approach is to allow the agent to decide for itself when to create a memory. In this pattern, memory generation is exposed as a tool (i.e. `create\_memory` ); the tool definition should define what types of information should be considered meaningful. The agent can then analyze the conversation and autonomously decide to call this tool when it identifies information that is meaningful to persist. This shifts the responsibility for identifying "meaningful information" from the external memory manager to the agent (and thus you as the developer) itself.

For example, you can do this using ADK by packaging your memory generation code into a Tool 21  that the agent decides to invoke when it deems the conversation meaningful to persist. You can send the Session to Memory Bank, and Memory Bank will extract and consolidate memories from the conversation history:

```
Python from google.adk.agents import LlmAgent from google.adk.memory import VertexAiMemoryBankService from google.adk.runners import Runner from google.adk.tools import ToolContext def generate_memories(tool_context: ToolContext): """Triggers memory generation to remember the session.""" # Option 1: Extract memories from the complete conversation history using the # ADK memory service. tool_context._invocation_context.memory_service.add_session_to_memory( session) # Option 2: Extract memories from the last conversation turn. client.agent_engines.memories.generate( name="projects/.../locations/...reasoningEngines/...", direct_contents_source={ "events": [ {"content": tool_context._invocation_context.user_content} ] }, scope={ "user_id": tool_context._invocation_context.user_id, "app_name": tool_context._invocation_context.app_name }, # Generate memories in the background config={"wait_for_completion": False} ) return {"status": "success"} agent = LlmAgent( ..., tools=[generate_memories] ) runner = Runner( agent=agent, app_name=APP_NAME, session_service=session_service, memory_service=VertexAiMemoryBankService( agent_engine_id=AGENT_ENGINE_ID, project=PROJECT, location=LOCATION ) )
```

Snippet 8: ADK agent using a custom tool to trigger memory generation. Memory Bank will extract and consolidate the memories.

Another approach is to leverage internal memory, where the agent actively decides what to remember from a conversation. In this workflow, the agent is responsible for extracting key information. Optionally, these extracted memories are then sent to Agent Engine Memory Bank to be consolidated with the user's existing memories 22 :

```
Python def extract_memories(query: str, tool_context: ToolContext): """Triggers memory generation to remember information. Args: query: Meaningful information that should be persisted about the user. """ client.agent_engines.memories.generate( name="projects/.../locations/...reasoningEngines/...", # The meaningful information is already extracted from the conversation, so we # just want to consolidate it with existing memories for the same user. direct_memories_source={ "direct_memories": [{"fact": query}] }, scope={ "user_id": tool_context._invocation_context.user_id, "app_name": tool_context._invocation_context.app_name }, config={"wait_for_completion": False} ) return {"status": "success"} agent = LlmAgent( ..., tools=[extract_memories] )
```

Snippet 9: ADK agent using a custom tool to extract memories from the conversation and trigger consolidation with Agent Engine Memory Bank. Unlike Snippet 8, the agent is responsible for extracting memories, not Memory Bank.
