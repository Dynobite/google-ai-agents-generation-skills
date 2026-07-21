## Skill Anatomy  &amp; Progressive Disclosure

Before going into the different paths, let's review the Skill anatomy. Every skill lives in its own directory and must contain a SKILL.md . To see the full canonical structure, as defined by the open standard at agentskills.io , let's look at a practical example.

Below is an illustrative folder for a Skill designed to conduct daily cafe preparation. (Remember, the only mandatory file is SKILL.md . The rest is optional):

```
cafe-preparation/ ├── SKILL.md # Required: metadata + instructions ├── scripts/ # Optional: executable code (any language) │   ├── calc_quantities.py # Estimates lattes, croissants, etc. │   └── convert_to_ingredients.py # Converts drinks and pastries into.. ├── references/ # Optional: supplementary context │   ├── menu_and_recipes.md # Matcha latte: 3g powder, 200ml... │   └── minimums.md # Always prep for at least 40 lattes... └── assets/ # Optional: templates, configs, schemas ├── prep_sheet_template.md # The final layout for the kitchen staff └── shopping_list_template.md # The layout for vendor ordering
```

Snippet 1: Directory tree structure showing the standard layout and progressive disclosure design for the cafe-preparation skill.

The innovative piece is the progressive disclosure . Skills load in three levels:

1.  Metadata (name + description) is always in the agent's context.
2.  SKILL.md body is loaded only when the skill triggers.
3.  Bundled resources are loaded strictly as needed (and scripts execute without ever polluting the token window).

This means you can have a hundred installed skills but only pay the tiny token cost for their metadata on every turn. Let's get practical and look at how to build one.
