## 8. How to Decide Among the Hundreds of Skills That Exist

By early 2026, public skill marketplaces had crossed 40,000 listings, with the leading platform reporting tens of thousands of new skills published in the first weeks of January alone. At Google Cloud Next 2026, Google launched its official Agent Skills repository at github.com/google/skills , with skills installable via npx skills install github. com/google/skills for use across Antigravity CLI, and any other coding agent that supports the Skills standard. The Anthropic skills repository, the Google ADK skill library, the Google official skills repository, and community marketplaces such as awesome-llm-apps now host more skills than any practitioner could review individually. The selection problem is real and growing.

Three heuristics help.

1.  First, prefer first-party skills for vendor-specific tools. Google's BigQuery skill, the official Stripe skill, anything written by the people who built the underlying system. They will be more correct and more maintained than community alternatives.

2.  Second, pin everything you depend on. Community skills evolve, and an unpinned dependency that worked yesterday can fail tomorrow.
3.  Third, audit before adopting. A skill is code that runs in your context. Treat it like any other dependency, with the same supply-chain hygiene.

Not all sources are equal. Three categories of skill source exist in early 2026, and the right operational stance is different for each:

Table 4: Overview of Agent Skill sources categorized by trust defaults, official examples, and maintenance ownership.

| Source                      | Trust default                            | Examples                                                                                                                               | Who maintains it                                  |
|-----------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| First-party vendor skills   | Trust by default; pin a version          | google/agents-cli 28 , google/ skills 29 , google-gemini/gemini- skills 30 , anthropics/skills 31 , stripe/ai 32 , microsoft/skills 33 | The team that built the underlying product        |
| Organization-curated skills | Trust within the org; review on adoption | your-org/retail-skills, your- org/finance-skills (private, internally maintained)                                                      | Your own domain teams, with PR review             |
| Community skills            | Audit before adopting; pin aggressively  | VoltAgent/awesome-agent- skills 34 , SkillsMP marketplace 35 , addyosmani/agent-skills 36 , individual GitHub repos                    | Volunteer authors, varying maintenance commitment |
