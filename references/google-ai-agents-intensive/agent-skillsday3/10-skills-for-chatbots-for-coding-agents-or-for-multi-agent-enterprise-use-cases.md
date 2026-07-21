## Skills for chatbots, for coding agents, or for multi-agent enterprise use cases?

The first publicly visible skills were AI chatbot-shaped. The coding-agent narrative arrived within days or weeks. And once it did, skills exploded. They landed straight into the vibecoding fever and turned out to be the format developers had been wanting.

In some multi-agentic architectures, by definition, each sub-agent is already a specialist. A research agent might not need a research skill. Skills are more useful in scenarios when one general-purpose agent has the flexibility to become a specialist across different things, by design. However, there might be cases where multi-agent and skills do compose well, for example, if there is a need for each specialized agent to have its own scoped skill library.

Now consider a logistics company with 100  process variants depending on product type, tools, route constraints, customer SLAs, regulatory zones, etc. How could this be solved elegantly and lightweight:

- One agent, one giant context window . Causes immediate context rot and exorbitant token costs.
- RAG over the runbooks . Probably the right answer two years ago. But you're now running a vector DB, an embedding model, and a chunking strategy whose quality has nothing to do with the actual procedures.
- Multi-agent, one subagent per process . 100 subagents, each with a process-specific system prompt. An operational nightmare of 100 deployments, 100 evaluation surfaces, and complex routing layers.
- One agent, 100 skills . This fits the skills format as there are many variants for the same job. The progressive disclosure of skills means 100 skills cost ~100 × 50 tokens = ~5,000 tokens of always-loaded metadata. Logistics requests carry strong activation cues: SKU, origin, weight, hazmat flag, SLA, which makes skill descriptions sharp and selection reliable. Procedures live in version control. Adding the 101st variant is a new folder, not a new deployment. Easier to maintain and to scale.

However, the most important part is to always have a strict evaluation process and compare different performances to make the final decision ( Section 4 covers what that evaluation work actually looks like in practice).

As a mental note, adoption follows the path of least resistance. Anyone who can write documentation can write a skill. That lowers the barrier and the latent procedural knowledge sitting in wikis, runbooks, and engineers' heads finally has somewhere structured to flow.
