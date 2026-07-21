## Memories in the System Instructions

A simple option to use memories for inference is to append memories to the system instructions. This method keeps the conversation history clean by appending retrieved memories directly to the system prompt alongside a preamble, framing them as foundational context for the entire interaction. For example, you can use Jinja to dynamically add memories to your system instructions:

```
Python from jinja2 import Template template = Template(""" {{ system_instructions }}} <MEMORIES> Here is some information about the user: {% for retrieved_memory in data %}* {{ retrieved_memory.memory.fact }} {% endfor %}</MEMORIES> """) prompt = template.render( system_instructions=system_instructions, data=retrieved_memories )
```

Snippet 12: Build your system instruction using retrieved memories

Including memories in the system instructions gives memories high authority, cleanly separates context from dialogue, and is ideal for stable, "global" information like a user profile. However, there is a risk of over-influence , where the agent might try to relate every topic back to the memories in its core instructions, even when inappropriate.

This architectural pattern introduces several constraints. First, it requires the agent framework to support dynamic construction of the system prompt before each LLM call; this functionality isn't always readily supported. Additionally, the pattern is incompatible with "Memory-as-a-Tool' given that the system prompt must be finalized before the LLM can decide to call a memory retrieval tool. Finally, it poorly handles non-textual memories. Most LLMs only accept a text for the system instructions, making it challenging to embed multimodal content like images or audio directly into the prompt.
