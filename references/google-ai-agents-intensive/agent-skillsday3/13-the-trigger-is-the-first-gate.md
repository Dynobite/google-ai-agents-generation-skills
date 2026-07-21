## The trigger is the first gate

A skill that never fires cannot help. A skill that fires too broadly injects irrelevant context.

Vercel's production analysis 8  revealed a 56% non-invocation rate for skills expected to activate consistently. More critically, a skill stripped of its instructions scored 58%, while the agent without the skill scored 63%. This 5-point deficit demonstrates that a poorly-designed skill can actively subtract capability.

In this same study, Vercel also noted that a passive AGENTS.md index of project conventions achieved a 100% pass rate against a 53% baseline. This reinforces that skills are best reserved for narrow, action-specific workflows, whereas global context should remain in passive, always-accessible documentation.

Now, to hit the industry-standard 90% trigger accuracy rate, your SKILL.md description, the only thing the model sees during routing, must pass four checks:

- Testable specificity: You must write 3 positive and 3 negative triggers.
- Clarity: Ambiguous queries don't overlap with adjacent skills.
- Execution fidelity: It describes actual performance, not aspirational behavior.
- Rephrasing stability: It routes consistently regardless of how the user phrases the intent.
