## Triggering memory generation

Although memory managers automate memory extraction and consolidation once generation is triggered, the agent must still decide when memory generation should be attempted. This is a critical architectural choice, balancing data freshness against computational cost and latency. This decision is typically managed by the agent's logic, which can employ several triggering strategies. Memory generation can be initiated based on various events:

- Session Completion: Triggering generation at the end of a multi-turn session.

- Turn Cadence: Running the process after a specific number of turns (e.g., every 5 turns).
- Real-Time: Generating memories after every single turn.
- Explicit Command: Activating the process upon a direct user command (e.g., "Remember this"

The choice of trigger involves a direct tradeoff between cost and fidelity. Frequent generation (e.g., real-time) ensures memories are highly detailed and fresh, capturing every nuance of the conversation. However, this incurs the highest LLM and database costs and can introduce latency if not handled properly. Infrequent generation (e.g., at session completion) is far more cost-effective but risks creating lower-fidelity memories, as the LLM must summarize a much larger block of conversation at once. You also want to be careful that the memory manager is not processing the same events multiple times, as that introduces unnecessary cost.
