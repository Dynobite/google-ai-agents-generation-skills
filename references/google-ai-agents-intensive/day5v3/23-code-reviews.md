## Code Reviews

To survive the volume and scale of AI-generated commits without burnout, teams will need to explore new guidelines. While the ideal workflow is subject to debate, here are some ideas to help manage the shift from writing code to integrating it:

Strategies for High-Velocity Integration

- Bundled Summaries and Risk Assessments: Consider requiring every PR to include an AI-generated snapshot of what changed, potential breakage points, and a risk assessment. This could be a markdown file or a detailed commit description that helps human reviewers focus on architectural impact rather than getting lost in the lines.

- Reimagined Ownership: Shift the focus of human reviews from nitpicking style on disposable, agent-written code to ensuring the integrity of the architectural blueprints. Style concerns can be addressed through automated integration tools like shared syntax linters or workspace-specific stylebooks (e.g., SKILLS.md).
- The "Conditional LGTM": To eliminate 12-hour delays in cross-timezone teams, you might institute a "Conditional LGTM" (Looks Good To Me). A reviewer approves the PR contingent on it passing all automated tests; if the tests turn green, the code merges automatically.
- Defining a No-Blame Culture: In high-velocity environments, the person producing the most code often becomes a scapegoat for bugs or merge conflicts. It is helpful to discuss how to attribute these issues to broken integration processes rather than the individual developer using the agent.
- The Usage of Agent Coding Reviews: You could build a skill which does the code review for you. And you can even write skills that respond to code reviews. See Code Snippet 5.1. You can automate this with Github Actions 6  or using Gemini Code Assist on Github 7 .

Lastly, you could even wonder and discuss; if you can work with a squad of agents, do you even need to work as a team at all? But if you decide you do, you might explore ways to split work so that team members rarely touch the same files-for example, assigning clear ownership over APIs versus UX. When overlap is necessary, the designated "part owner" can handle the final synchronization.

```
Act as a Senior Software Engineer and Security Researcher. Review the provided code for this Github PR or Diff using these strict criteria: Use the command line to fetch the Github PR: `gh pr view <PR NUMBER>` First analyze the code, then code review: 1. **Critical Vulnerabilities:** Check for hardcoded secrets (API keys), SQL injection, XSS, or broken authentication. 2. **Logic & Efficiency:** Identify "off-by-one" errors, infinite loops, or redundant API calls. 3. **Readability:** Suggest better naming conventions or breaking down "megafunctions" into smaller pieces. 4. **Edge Cases:** What happens if the input is null? What if the network fails? Output Format: - **Description:** - What is this PR doing? Explain in details. ISSUES: -⚠ **Critical:** (Stop-ship issues) -⚠️ **Warnings:** (Code smells or style issues) -✅ **Best Practices:** (Specific lines to refactor for better performance) -💡 **Quick Win:** (One sentence summary of the biggest improvement) When there are no issues return - **Description:** - What is this PR doing? Explain in details. LGTM
```

Snippet 3: code-check.md: This skill defines a structured workflow for automated code reviews against security and logic criteria.
