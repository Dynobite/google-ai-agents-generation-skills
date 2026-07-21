## Observability: Auditing the Agent's Mind (Pillar 6 &amp; 7)

To effectively secure and evaluate a vibe-coded agent, we must acknowledge a fundamental rule: you cannot secure what you cannot see. In traditional microservices, an HTTP 200 OK status indicates a successful operation. However, in an agentic system, a "success" status might merely mask a scenario where the agent's internal logic has quietly cascaded into a hallucination loop. This introduces the critical risk of Denial of Wallet (DoW) attacks, where adversaries intentionally trigger infinite, computationally expensive API loops to deliberately bankrupt the organisation's cloud and LLM billing accounts.

Observability is no longer merely an operational concern for uptime and latency; it is a strict security requirement to illuminate the "glass box" of non-deterministic logic.
