## Procedural memories

This whitepaper has focused primarily on declarative memories, a concentration that mirrors the current commercial memory landscape. Most memory management platforms are also architected for this declarative approach, excelling at extracting, storing, and retrieving the "what"-facts, history, and user data.

However, these systems  are not designed to manage procedural memories, the mechanism for improving an agent's workflows and reasoning. Storing the "how" is not an information retrieval problem; it is a reasoning augmentation problem. Managing this "knowing how" requires a completely separate and specialized algorithmic lifecycle, albeit with a similar high-level structure 26 :

1.  Extraction: Procedural extraction requires specialized prompts designed to distill a reusable strategy or "playbook" from a successful interaction, rather than just capturing a fact or meaningful information.
2. Consolidation: While declarative consolidation merges related facts (the "what"), procedural consolidation curates the workflow itself (the "how"). This is an active logic management process focused on integrating new successful methods with existing "best practices," patching flawed steps in a known plan, and pruning outdated or ineffective procedures.
3.  Retrieval: The goal is not to retrieve data to answer a question, but to retrieve a plan that guides the agent on how to execute a complex task. Therefore, procedural memories may have a different data schema than declarative memories.

This capacity for an agent to 'self-evolve' its logic naturally invites a comparison to a common adaptation method: fine-tuning-often via Reinforcement Learning from Human Feedback (RLHF) 27 . While both processes aim to improve agent behavior, their mechanisms and applications are fundamentally different. Fine-tuning is a relatively slow, offline training process that alters model weights. Procedural memory provides a fast, online adaptation by dynamically injecting the correct "playbook" into the prompt, guiding the agent via in-context learning without requiring any fine-tuning.
