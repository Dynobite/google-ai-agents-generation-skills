## The quality principles

1.  Run the task yourself first . Real failure produces signal. Speculation produces noise.
2. Give the reason, not just the rule . Models generalize wonderfully to edge cases when they understand why an instruction exists. If you find yourself typing "ALWAYS" or "NEVER" in caps, pause and try explaining the rationale instead.
3.  Every line should earn its place . Keep gotchas, exact commands, business logic, antipatterns. Cut boilerplate the model already knows such as "always validate output".
4. One skill, one job . If the description needs "and" between unrelated capabilities, split it.
5.  Make instructions verifiable . If the agent can't tell whether it followed the rule, the rule is too vague.
6.  Bundle what repeats . Helper code the agent keeps re-deriving belongs in scripts/ .
