## The Green Team (Agent Fixer): Quarantine and Auto-Refactoring

When the Blue Team detects a compromised agent, traditional incident response methodssuch as aggressively killing the host container-are highly disruptive and dangerous. Terminating an agent mid-thought can leave connected APIs in a corrupted state. Instead, the automated Green Team executes a "Stateful Quarantine" via SOAR playbooks. This gracefully revokes the agent's specific tool access, freezing its ability to act upon the world while preserving its short-term memory entirely intact for forensic analysis.

Furthermore, the Green Team goes a step further by performing Auto-Refactoring . Leveraging the system's innate capacity for self-repair, the Agent Fixer autonomously rewrites the insecure, vibe-coded script to patch the vulnerability. It then presents the secure, alternative code back to the developer directly within their IDE, requiring no manual human intervention to formulate the fix.
