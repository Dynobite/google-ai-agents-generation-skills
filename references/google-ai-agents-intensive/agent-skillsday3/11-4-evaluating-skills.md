## 4. Evaluating Skills

Now you have a first skill, or maybe a small library of them. The question that immediately follows is: how do you know they actually work? How skills fail, how to test them, and the four conditions every skill should pass before it earns a place in your library.

An Agent Skill without a test is a hope, not a capability.

When researchers recently benchmarked 84 real-world agent tasks in SkillsBench (2025) 7 , they found that 19% performed worse with a skill than without one. These poorly designed skills were not just neutral noise, they actively degraded capability. Fortunately, these failures are predictable and fall into four distinct modes:

1.  Trigger Failure: The wrong skill fires, or the correct one fails to fire.
2. Execution Failure: The skill triggers correctly, but produces incorrect output or errant tool calls.
3.  Token Budget Failure: A massive skill body crowds the context window, degrading performance on unrelated turns.
4. Regression: A newly added skill overlaps with an existing one, breaking previously working routing.

Trigger failures surface in routing logs; execution failures in output quality; token budget failures under realistic context load; regression failures only when the full library is exercised together.

Figure 1: Notice how the failure modes branch out. Trigger and execution failures happen on a single-turn level, while token budget and regression failures only appear when multiple skills interact under a heavy production load.

<!-- image -->
