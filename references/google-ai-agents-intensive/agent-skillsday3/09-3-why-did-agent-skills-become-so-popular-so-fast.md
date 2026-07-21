## 3. Why did Agent Skills become so popular, so fast?

Imagine it's early 2025. You are asked to build a system that offload repetitive back office work: generating slide decks from briefs while adhering to the company style, parsing structured invoicing PDFs, drafting HR onboarding guides, summarising weekly compliance reports, and tackling a long tail of similar tasks that will inevitably grow as the team finds new things to automate.

Most likely, you would have defaulted to a multi-agent architecture. A router agent at the top dispatching to a handful of specialist sub-agents beneath it. You would then spend agonizing hours on CI/CD pipelines, orchestration logic, and ensuring that a deployment for the new HR sub-agent didn't break the invoice sub-agent.

With the release of Agent Skills, this workflow becomes vastly simpler. This friction is exactly how the Skill format was first created by Anthropic, with the first skills for reading PDFs and creating slides 6 , which represents a much lighter version to accomplish this. Instead of a router dispatching subagents, you have one agent with a library of skills. Skills can run commands, call MCP servers, and bundle Python scripts. The agent decides which to load when. You maintain skills, not agents, and the operational surface can shrink.

To be very clear: Agent Skills do not kill multi-agent architectures.

Multi-agent remains the absolute right answer when you have genuine parallelism, real capability boundaries (different access, different security postures, different external systems), hierarchical decomposition where the abstraction layers actually differ, adversarial or check-and-balance setups, sub-agent intercommunication, or heterogeneous models. This list isn't exhaustive.

What Skills did was introduce a missing architectural primitive. Many systems that were built multi-agent by default can now be elegantly simplified to single-agent-with-skills by design .
