## Inference with Memories

Once relevant memories have been retrieved, the final step is to strategically place them into the model's context window. This is a critical process; the placement of memories can significantly influence the LLM's reasoning, affect operational costs, and ultimately determine the quality of the final answer.

Memories are primarily presented by appending them to system instructions or injecting them into conversation history. In practice, a hybrid strategy is often the most effective. Use the system prompt for stable, global memories (like a user profile) that should always be present. Otherwise, use dialogue injection or memory-as-a-tool for transient, episodic memories that are only relevant to the immediate context of the conversation. This balances the need for persistent context with the flexibility of in-the-moment information retrieval.
