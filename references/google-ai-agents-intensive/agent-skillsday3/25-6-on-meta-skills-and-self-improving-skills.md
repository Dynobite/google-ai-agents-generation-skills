## 6. On Meta-Skills and Self-Improving Skills

So far, every skill in this document has been written by a human. A domain expert sits down, drafts a SKILL.md, tests it, ships it. That's the right place to start. But once you have a working library, the natural next question is: can the agent help write, evaluate, and improve skills too?

This is the meta-skills territory. Skills whose job is to author, evaluate, or improve other skills. In practice, these "meta-skills" fall into four buckets:

1.  Authoring . Skills that take a description of a workflow and produce a draft SKILL.md. Google's ADK 21  has a "skill factory" pattern that does this through its SkillToolset . Anthropic ships a skill-creator Skill 22  that walks you through creation, evaluation, and tuning.
2. Assisted authoring from traces . Instead of asking a human to describe a workflow, watch the agent do it successfully a few times, then turn that trace into a skill. The skillcreator workflow supports this directly through trace-based harvesting. The human's job shifts from writing the skill to confirming that the harvested version captures the right steps.
3.  Improvement . Skills that take an existing skill plus a set of failing evaluation cases and propose edits. Saboo's SkillOptimizer 24  and Anthropic's description-optimization loop are both examples. Another is Karpathy's autoresearch pattern 25 , where an agent proposes a change to a target file, runs a bounded experiment, and keeps the change only if a metric improves.

Figure 9: The step-by-step loop demonstrates how real, successful production histories are transformed into reliable procedural memories without manual human drafting

<!-- image -->

Figure 10: Notice the evaluation gating. The agent can suggest changes to descriptions or instructions, but it cannot commit them to the library unless the unit tests pass.

<!-- image -->

4. Library evolution . Skills that grow the library over time, the way Voyager grew its own Minecraft skill library 26 . The agent finishes a task it had no skill for, notices that it just solved a recurring problem, and proposes adding a new skill to cover it. Schmid's selflearning-skill 27  is a community reference implementation of this pattern.
