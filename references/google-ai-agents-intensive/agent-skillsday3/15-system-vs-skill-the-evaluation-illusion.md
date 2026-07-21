## System vs. Skill: The Evaluation Illusion

Trajectory testing evaluates the composite system of the host agent interacting with the skill rather than the skill in isolation. When a multi-skill trajectory fails, it is often impossible to decouple agent routing, instruction quality, or execution fidelity. To simplify calibration, evaluate skills via a "Single-Skill Sub-Agent pattern" (Agent + 1 Skill vs. Base Agent); save complex multi-skill co-loading for advanced production staging.

Evaluation-Driven Development (EDD) 11  inverts the workflow by writing three JSON evaluation cases (Input, Expected Tools, Expected Output) before drafting the SKILL.md . It forces a clear functional spec upfront.This forces a clear functional specification upfront. A minimal eval case looks like this:

```
JSON { "case_id": "refund_dup_charge_001", "input": "I was charged twice for order #4521 last Tuesday", "expected_skill": "refund_processor", "expected_tool_calls": [ {"tool": "lookup_order", "args": {"order_id": "4521"}}, {"tool": "check_duplicate_charge", "args": {"order_id": "4521"}} ], "expected_output_format": "confirmation_with_refund_id", "rubric": ["acknowledges duplicate", "cites order id", "provides next step"] }
```

Snippet 3: A minimal JSON evaluation case example used in Evaluation-Driven Development (EDD) to explicitly define input parameters, expected tool trajectories, and evaluation rubrics upfront.

Drafting three such cases upfront surfaces description ambiguities and tool-trajectory errors before they compound in the skill body.

When using LLM-as-Judge to score outputs at scale, remember two non-negotiables: swap the positions of the reference and actual outputs to eliminate ordering bias, and calibrate against human ratings until you hit 90% agreement.
