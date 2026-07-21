## Organization patterns

Once a memory is created, the next question is how to organize it. Memory managers typically employ one or more of the following patterns to organize memories: Collections 12 , Structured User Profile , or 'Rolling Summary' .  The patterns define how individual memories relate to each other and to the user.

The collections 13  pattern organizes content into multiple self-contained, natural language memories for a single user. Each memory is a distinct event, summary, or observation, although there may be multiple memories in the collection for a single high-level topic. Collections allow for storing and searching through a larger, less structured pool of information related to specific goals or topics.

The structured user profile pattern organizes memories as a set of core facts about a user, like a contact card that is continuously updated with new, stable information. It's designed for quick lookups of essential, factual information like names, preferences, and account details.

Unlike a structured user profile, the 'rolling' summary pattern consolidates all information into a single, evolving memory that represents a natural-language summary of the entire user-agent relationship. Instead of creating new, individual memories, the manager continuously updates this one master document. This pattern is frequently used to compact long Sessions, preserving vital information while managing the overall token count.
