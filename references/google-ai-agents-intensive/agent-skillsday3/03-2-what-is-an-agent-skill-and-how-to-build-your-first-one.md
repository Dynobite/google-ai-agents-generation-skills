## 2. What is an Agent Skill (and How to Build Your First One)

Agent Skills are a primitive for giving a general-purpose agent on-demand specialist competence. Yes, a Skill can be as simple as a single markdown file, but it doesn't have to stop there, and the paradigm behind it is quite innovative.

Today we are seeing Agent Skills emerge through two distinct  patterns:

The first path is driven by subject matter experts , who already have institutional knowledge written down somewhere. Think of a compliance officer with a 30-page runbook, or an HR manager with onboarding guides for new hires. None of them need to learn to code to write and start using a Skill. They already have the content; the only job left is to translate it into a format the agent can use smartly.

The second path involves developers wrapping agentic or coded workflows into Skills. If an agent successfully executes a non-trivial, repetitive task, you don't want it to have to figure out the process from scratch next time. Instead, you want the agent to create a Skill out of this successful run. In short, we are observing an emerging pattern: anything that is a good, reusable workflow becomes a Skill, and you don't have to write it yourself, the agent does, you review. This is already meta-skills territory, which we introduce gently here before going deep on it in Section 6 .

Both groups produce the same artifact, a Skill folder anchored by the SKILL.md primitive, but the journey to get there is different.
