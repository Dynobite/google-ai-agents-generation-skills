## 2. Agent Skills (Reusable, Feature/Behavior-focused)

Skills are structured Markdown files containing specialized, trigger-based workflows. While skills can live anywhere in the repository, they must be stored in the designated .agent directory to be recognized by the Antigravity workspace manager. They teach the agent repeatable engineering habits-like automatically maintaining a CHANGELOG.md when code changes are detected.

./my-app/ .agent/skills/docs-maintenance/SKILL.md Such a skills folder, can also contain data assets or scripts, for the skill to use.

3. System Prompts (Global, Identity-focused)

This is where the AI learns the specific engineering DNA. Both Gemini CLI and Google Antigravity scan and concatenate context files hierarchically, meaning custom instructions are layered from global overrides down to local project configurations.

- The Global Profile: This file lives in the home configuration directory (e.g., ~/.gemini/ GEMINI.md). This is where the AI becomes more aligned with individual preferences. It defines a universal persona, default style, and core principles, regardless of the project.
- The Shared Multi-Tool Config (AGENTS.md): To prevent instructional fragmentation if a team uses multiple AI clients, the ecosystem supports AGENTS.md. This acts as a shared cross-tool foundation, while a local GEMINI.md file retains the highest priority for Google-specific settings.

./my-app/ .agents/AGENTS.md)

- The Project Spec: This file lives in the project's root directory (e.g., ./my-app/.gemini/ GEMINI.md). This is the project's DNA. The CLI agent automatically detects and reads this file, prioritizing its rules.
