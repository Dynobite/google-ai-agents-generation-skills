## Output quality and tool trajectory

Once a skill triggers, test both the final output (what the agent says) and the tool trajectory (what the agent does) separately.

A smart way to do this is to use the Evaluation-Driven Development (EDD) . Invert the workflow by writing three JSON evaluation cases (Input, Expected Tools, Expected Output) before drafting the SKILL.md . It forces a clear functional spec upfront. When using LLM-asJudge to score outputs at scale, remember two non-negotiables: swap the positions of the reference and actual outputs to eliminate ordering bias, and calibrate against human ratings until you hit 90% agreement.

Latitude's analysis (March 2026) 9  found that final-output-only scoring passes 20% to 40% more cases than trajectory-aware scoring. This gap represents instances where the agent reached the correct answer via an incorrect sequence of tool calls. Acceptable in readonly scenarios. Critical in action-allowed skills, where incorrect tool trajectories can cause irreversible side effects.

The Google ADK eval framework 10  offers three trajectory scoring modes: EXACT (exact order), IN\_ORDER (ordered subset), and ANY\_ORDER (unordered subset). Trajectory validation should align with the skill tier: read-only skills can use ANY\_ORDER, action-allowed skills require IN\_ORDER or EXACT.

Figure 3: Follow the inversion path. Instead of writing code first, the workflow forces you to define expected tool trajectories and evaluation rubrics as the very first step.

<!-- image -->
