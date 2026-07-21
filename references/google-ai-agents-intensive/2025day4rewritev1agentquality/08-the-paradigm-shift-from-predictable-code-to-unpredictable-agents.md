## The Paradigm Shift: From Predictable Code to Unpredictable Agents

The core technical challenge stems from the evolution from model-centric AI to systemcentric AI . Evaluating an AI agent is fundamentally different from evaluating an algorithm because the agent is a system. This evolution has occurred in compounding stages, each adding a new layer of evaluative complexity.

Figure 1: From Traditional ML to Multi-Agent Systems

<!-- image -->

1.  Traditional Machine Learning: Evaluating regression or classification models, while nontrivial, is a well-defined problem. We rely on statistical metrics like Precision, Recall, F1Score, and RMSE against a held-out test set. The problem is complex, but the definition of "correct" is clear.

2. The Passive LLM: With the rise of generative models, we lost our simple metrics. How do we measure the "accuracy" of a generated paragraph? The output is probabilistic. Even with identical inputs, the output can vary. Evaluation became more complex, relying on human raters and model-vs-model benchmarking. Still, these systems were largely passive, text-in, text-out tools.
3.  LLM+RAG (Retrieval-Augmented Generation): The next leap introduced a multicomponent pipeline, as pioneered by Lewis et al. (2020) 1 in their work "RetrievalAugmented Generation for Knowledge-Intensive NLP Tasks." Now, failure could occur in the LLM or in the retrieval system. Did the agent give a bad answer because the LLM reasoned poorly, or because the vector database retrieved irrelevant snippets? Our evaluation surface expanded from just the model to include the performance of chunking strategies, embeddings, and retrievers.
4. The Active AI Agent: Today, we face a profound architectural shift. The LLM is no longer just a text generator; it is the reasoning "brain" within a complex system, integrated into a loop capable of autonomous action. This agentic system introduces three core technical capabilities that break our evaluation models:
- Planning and Multi-Step Reasoning: Agents decompose complex goals ("plan my trip") into multiple sub-tasks. This creates a trajectory (Thought → Action → Observation → Thought...). The non-determinism of the LLM now compounds at every step. A small, stochastic word choice in Step 1 can send the agent down a completely different and unrecoverable reasoning path by Step 4.
- Tool Use and Function Calling: Agents interact with the real world through APIs and external tools (code interpreters, search engines, booking APIs). This introduces dynamic environmental interaction. The agent's next action depends entirely on the state of an external, uncontrollable world.

-  Memory: Agents maintain state. Short-term "scratchpad" memory tracks the current task, while long-term memory allows the agent to learn from past interactions. This means the agent's behavior evolves, and an input that worked yesterday might produce a different result today based on what the agent has "learned."
5.  Multi-Agent Systems: The ultimate architectural complexity arises when multiple active agents are integrated into a shared environment. This is no longer the evaluation of a single trajectory but of a system-level emergent phenomenon, introducing new, fundamental challenges:
- Emergent System Failures: The system's success depends on the unscripted interactions between agents, such as resource contention, communication bottlenecks, and systemic deadlocks, which cannot be attributed to a single agent's failure.
- Cooperative vs. Competitive Evaluation: The objective function itself may become ambiguous. In cooperative MAS (e.g., supply chain optimization), success is a global metric, while in competitive MAS (e.g., game theory scenarios or auction systems), the evaluation often requires tracking individual agent performance and the stability of the overall market/environment.
- To address these systemic challenges, the Agent Development Kit (ADK) introduces a graph-based framework that allows engineers to organize agents into structured networks of sub-agents. This shifts development from loose prompt-chaining to deterministic, path-based delegation, ensuring critical compliance and governance steps are rigidly enforced while leveraging generative planning where safe.

This combination of capabilities means the primary unit of evaluation is no longer the model, but the entire system trajectory . The agent's emergent behavior arises from the intricate interplay between its planning module, its tools, its memory, and the dynamic environment.
