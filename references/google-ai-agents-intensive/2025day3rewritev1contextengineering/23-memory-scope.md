## Memory scope

You also need to consider who or what a memory describes. This has implications on what entity (i.e. a user , session , or application ) you use to aggregate and retrieve memories.

User-Level scope is the most common implementation, designed to create a continuous, personalized experience for each individual; for example, 'the User prefers the middle seat.' Memories are tied to a specific user ID and persist across all their sessions, allowing the agent to build a long-term understanding of their preferences and history.

Session-Level scope is designed for the compaction of long conversations; for example, 'the User is shopping for tickets between New York and Paris between November 7, 2025 and November 14, 2025. They prefer direct flights and the middle seat' . It creates a persistent record of insights extracted from a single session, allowing an agent to replace the verbose, token-heavy transcript with a concise set of key facts. Crucially, this memory is distinct from the raw session log; it contains only the processed insights from the dialogue, not the dialogue itself, and its context is isolated to that specific session.

Application-level scope (or global context), are memories accessible by all users of an application; for example, 'The codename XYZ refers to the project….' This scope is used to provide shared context, broadcast system-wide information, or establish a baseline of common knowledge. A common use case for application-level memories is procedural memories , which provide "how-to" instructions for the agent; the memories are generally intended to help with the agent's reasoning for all users. It is critical that these memories are sanitized of all sensitive content to prevent data leaks between users.
