## The Spectrum

The three tiers differ in who owns the runtime and who writes the review criteria:

- Tier 1 - Managed (e.g. Gemini Code Assist on GitHub [8], or any SaaS PR reviewer) . The off-the-shelf path. Enable it on your GitHub or GitLab org and every PR gets an AI reviewer that comments on style, bugs, and security out of the box. No prompts to write, no infrastructure to manage; pay per seat. The trade: you get the vendor's review opinions, not yours - a generic reviewer will miss what matters to a team with a strict house style or a domain-specific risk profile (HIPAA, PCI, internal SDKs).
- Tier 2 - Hybrid (e.g. a GitHub Action 6 triggering a coding agent CLI - Antigravity CLI 12 ) . The middle path, and the right starting point for most teams. Write your own review skill - the code-check.md from earlier in this paper is a working example - commit it

to the repo, and trigger it from a CI action that runs the CLI of choice in non-interactive mode and posts the result as a PR comment. The runtime belongs to your CI provider; the prompts, model choice, sandboxing, and review criteria belong to you.

- Tier 3 - Custom (e.g. an ADK agent on Gemini Enterprise Agent Engine 9 ) . The fully owned path. For example you can set the reviewer as an ADK agent, deploy it to Agent Runtime for managed runtime with durable Sessions and Memory Bank, and wire it to webhook events from your source host. This is the right answer when the reviewer must hold context across a multi-PR refactor, decompose "audit this service for compliance drift" into a hundred sub-tasks via a planner-and-sub-agents pattern, or coordinate with other agents over A2A 10 . The trade: you own evaluation, observability, cost, and the on-call rotation when it fails in production. An example of such an architecture can be found in the Siemens case study 17 .

Three questions tell you which tier you need:

1.  How specific is your review criteria?
- Generic → Tier 1.
- Team- or repo-specific → Tier 2 or 3.
2.  Does the agent need to remember things across runs?
- No → Tier 1 or 2.
- Yes (codebase memory, cross-PR context) → Tier 3.
3.  What is the worst case if it goes wrong?
- A noisy comment → any tier.
- A merged regression or leaked secret → Tier 3 with the Policy Server pattern from the previous section in front of every tool call.

Most teams discover their tier the moment the managed reviewer misses something specific. A platform team at a mid-size fintech, for example, started on Tier 1 and quickly found their compliance reviewer flagging boilerplate that auditors had already signed off - while missing the one pattern that mattered, unmasked PII in log statements. A 40-line compliance-check. md skill wired to a GitHub Action (Tier 2) dropped the false-positive comments sharply within a week. Tier 3 has not yet been needed.
