## Deep-dive: Memory Extraction

The goal of memory extraction is to answer the fundamental question: "What information in this conversation is meaningful enough to become a memory?" This is not simple summarization; it is a targeted, intelligent filtering process designed to separate the signal (important facts, preferences, goals) from the noise (pleasantries, filler text).

"Meaningful" is not a universal concept; it is defined entirely by the agent's purpose and use case. What a customer support agent needs to remember (e.g., order numbers, technical issues) is fundamentally different from what a personal wellness coach needs to remember (e.g., long-term goals, emotional states). Customizing what information is preserved is therefore the key to creating a truly effective agent.

The memory manager's LLM decides what to extract by following a carefully constructed set of programmatic guardrails and instructions, usually embedded in a complex system prompt. This prompt defines what "meaningful" means by providing the LLM with a set of topic definitions.  With schema and template-based extraction, the LLM is given a predefined JSON schema or a template using LLM features like structured output 18 ; the LLM is instructed to construct the JSON using corresponding information in the conversation. Alternatively, with natural language topic definitions, the LLM is guided by a simple natural language description of the topic.

With few-shot prompting, the LLM is "shown" what information to extract using examples. The prompt includes several examples of input text and the ideal, high-fidelity memory that should be extracted. The LLM learns the desired extraction pattern from the examples, making it highly effective for custom or nuanced topics that are difficult to describe with a schema or a simple definition.

Most memory managers work out-of-the-box by looking for common topics, such as user preferences, key facts, or goals. Many platforms also allow developers to define their own custom topics, tailoring the extraction process to their specific domain. For example, you can customize what information Agent Engine Memory Bank considers to be meaningful to be persisted by providing your own topic definitions and few-shot examples 19 :

```
Python from google.genai.types import Content, Part # See https://cloud.google.com/agent-builder/agent-engine/memory-bank/set-up for more information. memory_bank_config = { "customization_configs": [{ "memory_topics": [ { "managed_memory_topic": {"managed_topic_enum": "USER_PERSONAL_INFO" }}, Continues next page...
```

```
{ "custom_memory_topic": { "label": "business_feedback", "description": """Specific user feedback about their experience at the coffee shop. This includes opinions on drinks, food, pastries, ambiance, staff friendliness, service speed, cleanliness, and any suggestions for improvement.""" } } ], "generate_memories_examples": { "conversationSource": { "events": [ { "content": Content( role="model", parts=[Part(text="Welcome back to The Daily Grind! We'd love to hear your feedback on your visit.")]) },{ "content": Content( role="user", parts=[Part(text= "Hey. The drip coffee was a bit lukewarm today, which was a bummer. Also, the music was way too loud, I could barely hear my friend.")]) }] }, "generatedMemories": [ {"fact": "The user reported that the drip coffee was lukewarm."}, {"fact": "The user felt the music in the shop was too loud."} ] } }] } agent_engine = client.agent_engines.create( config={ "context_spec": {"memory_bank_config": memory_bank_config } } )
```

Snippet 7: Customizing what information Agent Engine Memory Bank considers meaningful to persist

Although memory extraction itself is not 'summarization,' the algorithm may incorporate summarization to distill information. To enhance efficiency, many memory managers incorporate a rolling summary of the conversation directly into the memory extraction prompt 20 . This condensed history provides the necessary context to extract key information from the most recent interactions. It eliminates the need to repeatedly process the full, verbose dialogue with each turn to maintain context.

Once information has been extracted from the data source, the existing corpus of memories must be updated to reflect the new information via consolidation.
