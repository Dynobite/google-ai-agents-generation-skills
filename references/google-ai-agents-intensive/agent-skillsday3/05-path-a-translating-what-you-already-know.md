## Path A: Translating what you already know

A minimal SKILL.md template lives in Appendix A. You can copy it directly. The piece worth focusing on first is the YAML frontmatter, because it's the activation trigger:

```
---name: cafe-preparation description: | Calculates daily ingredient needs and generates prep sheets for cafe operations. Use when the user asks to estimate daily quantities, convert drinks to ingredients, or generate shopping lists. Do NOT use for employee shift scheduling or financial accounting. ---
```

Snippet 2: YAML frontmatter configuration for the cafe-preparation skill.

There are two things worth getting right from the start: naming and the description field.

Naming . When naming, be obvious and boring: use snake\_case for directories (e.g., bigquery\_ingestion ), kebab-case for skill names (e.g., pdf-processing ), and prefer the gerund form like managing-databases . Avoid generic names such as utils or tools and omit any internal jargon.

Description . This is your routing algorithm. It is the only thing the model sees to decide whether to load the Agent Skill. State what it does, front-load trigger keywords, be pushy if the model under-triggers, and explicitly state what it is not for.

Once the SKILL.md is drafted, you build out the rest of the folder. This is where progressive disclosure starts paying off. Anything that doesn't need to be in the SKILL.md body goes somewhere else:

- Scripts . Deterministic work (parsing exports, math, formatting) lives in scripts/. The model decides what to do; the script does the heavy lifting.
- References . Knowledge that is only relevant once the skill is running (domain principles, definitions, edge case handling) lives in references/ and loads on demand.
- Assets . Templates and schemas live in assets/.

Rule of thumb: if the SKILL.md is starting to get long, the next paragraph probably belongs in references/ and not in the body.

(Impatient? Appendix A offers a printable operational cheat sheet with curated Do's and Don'ts to guide your initial Skill development). 1
