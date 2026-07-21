## Agent Ops: A Structured Approach to the Unpredictable

As you build your first agents, you will be manually testing the behavior, over and over again.  When you add a feature, does it work?  When you fix a bug, did you cause a different problem?  Testing is normal for software development but it works differently with generative AI.

The transition from traditional, deterministic software to stochastic, agentic systems requires a new operational philosophy. Traditional software unit tests could simply assert output == expected ; but that doesn't work when an agent's response is probabilistic by design. Also, because language is complicated, it usually requires a LM to evaluate 'quality' - that the agent's response does all of what it should, nothing it shouldn't, and with proper tone.

Figure 5: Relationships between the operational domains of DevOps, MLOps, and GenAIOps from https://medium.com/@sokratis.kartakis/genai-in-production-mlops-or-genaiops-25691c9becd0

<!-- image -->

Agent Ops is the disciplined, structured approach to managing this new reality. It is a natural evolution of DevOps and MLOps, tailored for the unique challenges of building, deploying, and governing AI agents, turning unpredictability from a liability into a managed, measurable, and reliable feature. 24  For a more complete deep dive see the agent quality focused whitepaper in this series.
