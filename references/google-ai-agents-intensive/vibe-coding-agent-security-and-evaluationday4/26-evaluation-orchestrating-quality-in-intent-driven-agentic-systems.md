## Evaluation: Orchestrating Quality in Intent-Driven Agentic Systems

The previous sections covered the security controls that constrain what a vibe-coded agent can do.

Those controls don't answer the question the developer actually has: did the agent build what I asked for, and is it any good? A vibe-coded agent can pass every security check and still misread the developer's intent, ignore the project's conventions, or break an unrelated feature. Security tells you the agent stayed inside the boundary; evaluation tells you whether what happened inside that boundary is worth shipping.

The following sections are structured around three questions: why vibe coding evaluation is different from evaluating other software, what to evaluate, and how to evaluate it. The diagram below summarizes each layer; the rest of the whitepaper expands them.

Figure 2: The vibe coding agent evaluation framework

<!-- image -->

Two areas sit deliberately outside the scope of this framework, both warranting dedicated treatment: subjective evaluation of non-verifiable outputs, where quality is defined by user or enterprise preferences rather than ground truth; and the feedback loop from user corrections back into the model, the harness, or the eval suite to drive improvement.
