## The "Inside-Out" View: Trajectory Evaluation (The Glass Box)

Once a failure is identified, we move to the "Inside-Out" view. We analyze the agent's approach by systematically assessing every component of its execution trajectory:

1.  LLM Planning (The "Thought"): We first check the core reasoning. Is the LLM itself the problem? Failures here include hallucinations, nonsensical or off-topic responses, context pollution, or repetitive output loops.
2. Tool Usage (Selection &amp; Parameterization): An agent is only as good as its tools. We must analyze if the agent is calling the wrong tool, failing to call a necessary tool, hallucinating tool names or parameter names/types, or calling one unnecessarily. Even if it selects the right tool, it can fail by providing missing parameters, incorrect data types, or malformed JSON for the API call.
3.  Tool Response Interpretation (The "Observation"): After a tool executes correctly, the agent must understand the result. Agents frequently fail here by misinterpreting numerical data, failing to extract key entities from the response, or, critically, not recognizing an error state returned by the tool (e.g., an API's 404 error) and proceeding as if the call was successful.
4. RAG Performance: If the agent uses Retrieval-Augmented Generation (RAG), the trajectory depends on the quality of its retrieved information. Failures include irrelevant document retrieval, fetching outdated or incorrect information, or the LLM ignoring the retrieved context entirely and hallucinating an answer anyway.
5.  Trajectory Efficiency and Robustness: Beyond correctness, we must evaluate the process itself: exposing inefficient resource allocation, such as an excessive number of API calls, high latency, or redundant efforts. It also reveals robustness failures, such as unhandled exceptions.
6.  Multi-Agent Dynamics: In advanced systems, trajectories involve multiple agents. Evaluation must then also include inter-agent communication logs to check for misunderstandings or communication loops and ensure agents are adhering to their defined roles without conflicting with others.

By analyzing the trace, we can move from "the final answer is wrong" (Black Box) to "the final answer is wrong because …." (Glass Box). This level of diagnostic power is the entire goal of agent evaluation.

<!-- image -->
