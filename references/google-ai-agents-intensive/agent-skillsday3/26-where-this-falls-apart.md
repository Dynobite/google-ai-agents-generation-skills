## Where this falls apart

Meta-skills only work if your evaluation suite is good. An agent that's allowed to edit its own skills will happily optimize for whatever metric you point it at, including metrics that are easy to game. The Section 4 evaluation work is what keeps this honest. Without solid trigger accuracy tests, regression tests, and human spot-checks, an autonomous improvement loop will quietly make your library worse while reporting that it's getting better.

A few habits that have held up:

- Anything an agent writes enters the library at the draft tier , regardless of how confident the meta-skill is. It graduates through the same Read / Draft / Act ladder from Section 4 as any human-written skill.

- Keep a human in the loop for the first few edits . Even when the metric clearly improves, scan the diff. The kind of mistake an agent makes (overfitting the description to a few test cases, breaking a downstream skill it didn't know existed) is exactly the kind a human catches in 30 seconds.
- Don't start with meta-skills . Get the manual authoring loop working first. The fastest way to get a bad library is to point an agent at an empty folder and ask it to generate fifty skills.
