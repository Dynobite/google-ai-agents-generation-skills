## The Compound Evaluation Trap: Skill vs. Agent

Trajectory testing evaluates the composite system. The skill and the host agent together. If a test fails, avoid over-engineering the 'SKILL.md' for a specific model, which ruins portability. Instead, isolate execution logic from routing by using a "Two-Tiered Assert Framework": validate underlying tool code independently, and audit `SKILL.md` triggers across multiple model families to catch brittle, architecture-locked descriptions.

MCPVerse 12  noted an 18.2% accuracy drop in Claude-4-Sonnet due to tool proliferation and context attention competition. Additionally, Chroma Research (2025) 13  found that all frontier models degrade as input grows, particularly when hindered by co-loaded noise.

Figure 4: Look at the performance gap between a single running skill and 15 co-loaded skills. The curve illustrates why passing an isolated test is a false positive for production readiness.

<!-- image -->

Because of this, skills must graduate through strict tiers of authority:

- Read-Only: LLM-as-Judge eval; 90% trigger accuracy.
- Draft-Only (Human Review): Golden dataset of 20+ cases; human approval.
- Action-Allowed: Full adversarial red-teaming; sustained success across multiple runs (not just a single lucky pass); no rollback events; sustained pass^k.

pass^k measures consistent, rather than occasional, success by running the evaluation $k$ times and requiring success on every run. On tau-bench (Yao et al., 2024) 14 , GPT-4o scored 61% on pass^1 but dropped below 25% on pass^8, demonstrating that single-run success is a poor predictor of production reliability.

When calibrating these thresholds, two factors are critical:

1. Production Degradation: ReliabilityBench 15  shows that production performance typically drops 20% to 30% compared to offline benchmark pass@1 numbers.
2. Simulation Bias: Simulation-based evaluations can suffer from an optimistic bias of up to 9% (the "Lost in Simulation" 16 finding).

Consequently, human review of representative outputs remains the ultimate validation signal for action-allowed graduation.
