## 1. Introduction

Agent Skills are a way to equip your agent with knowledge and company context. An Agent Skill is a folder containing a SKILL.md file , with scripts/ , references/ , and assets/ directories. Section 2 covers the anatomy in detail.

Agent Skills are becoming the standard for cross-platform portability. But why the sudden adoption velocity? We believe Agent Skills tackle four main friction points in AI agent development:

1.  Too many instructions, worse results . Dumping every instruction you can think of into a single system prompt inevitably degrades Large Language Model (LLM) performance, a problem known as context rot. Skills solve this by loading exclusively on demand. Section 5 unpacks the research behind this.

2. Knowing how, not just knowing what . LLMs already have reasonable analogs for remembering what happened (episodic memory) and remembering facts (semantic memory). What they've lacked is a way to remember how to do things step by step, which is called procedural memory. Agent Skills can be seen as the first credible procedural memory primitive for LLM Agents.
3.  Multi-agent overload . The ecosystem was flooded with complex multi-agent systems that are notoriously hard to build and maintain. While still necessary for certain tasks, Skills allow a single general-purpose agent to seamlessly flex into many specialist roles. Section 3 develops this argument in depth, with a worked example.
4. Portability . A folder with a markdown file is a remarkably lightweight primitive. Any agent with filesystem access can use them, making them perfectly portable across a multivendor AI landscape.

In this whitepaper, we cater to two personas: Builders (those using Skills) and Developers (those creating, versioning, and managing them). We'll gently walk through what a Skill is and how to use it ( Sections 2 to 3 ), before diving into complex Developer topics like evaluation, production readiness, meta-skills, and composition ( Sections 4 to 8 ).

(Impatient? Appendix A offers a printable operational cheat sheet, and Appendix B walks through a retail case study).
