## What this means for the token budget

Progressive disclosure, covered in Section 2 , is the architectural answer: metadata for every skill loads at startup, a skill's body loads only when its description matches, and supporting files load only when the body references them.

The math is worth showing. Consider an agent with fifty distinct workflows. As a single system prompt, it loads 15,000 tokens every turn. As a skills library, it loads ~4,000 tokens of descriptions plus the ~2,000-token body of the one active skill with ~6,000 tokens total, with the other forty-nine bodies on disk. Anthropic has published examples where converting a workflow to skills cut active context from roughly 150,000 tokens to 2,000, a reduction of more than 98 percent.

Figure 8: Token economics: a single big prompt versus a fifty-skill library. The library has fifty units of capability available, but only the active body sits in context at any moment.

<!-- image -->

Three practical implications follow:

- Capacity is the wrong metric . A 1M-token window can show significant degradation at 50K tokens.
- Active context is a budget, not a vessel . Every token in front of the model takes attention from every other. Treat the system prompt the way infra teams treat memory: a finite resource, allocated deliberately.
- Skills resolve the constraint . They keep active context small while keeping available capability effectively unbounded.

Once a team has a working library, the questions shift from maintaining a single skill to evolution, composition, and the larger ecosystem.
