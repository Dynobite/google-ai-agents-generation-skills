## Interoperability across multiple agent frameworks

Figure 4: A2A communication across multiple agents that use different frameworks

<!-- image -->

A framework's use of an internal data representation introduces a critical architectural trade-off for multi-agent system: the very abstraction that decouples an agent from an LLM also isolates it from agents using other agent frameworks. This isolation is solidified at the persistence layer. The storage model for a Session typically couples the database schema directly to the framework's internal objects, creating a rigid, relatively non-portable conversation record. Therefore, an agent built with LangGraph cannot natively interpret the distinct Session and Event objects persisted by an ADK-based agent, making seamless task handoffs impossible.

One emerging architectural pattern architectural pattern for coordinating collaboration between these isolated agents is Agent-to-Agent (A2A) communication 8 . While this pattern enables agents to exchange messages, it fails to address the core problem of sharing rich, contextual state. Each agent's conversation history is encoded in its framework's internal schema. As a result, any A2A message containing session events requires a translation layer to be useful.

A more robust architectural pattern for interoperability involves abstracting shared knowledge into a framework-agnostic data layer, such as Memory. Unlike a Session store, which preserves raw, framework-specific objects like Events and Messsages , a memory layer is designed to hold processed , canonical information. Key information-like summaries, extracted entities, and facts-is extracted from the conversation and is typically stored as strings or dictionaries. The memory layer's data structures are not coupled to any single framework's internal data representation, which allows it to serve as a universal, common data layer. This pattern allows heterogeneous agents to achieve true collaborative intelligence by sharing a common cognitive resource without requiring custom translators.
