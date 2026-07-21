## Why skills are the unit of improvement

The naive theory of agent improvement is that better models produce better agents. In production, the model is the infrastructure and skills are the primitive that lets improvements ship. Each new skill is a small, owned, testable unit of capability (as we set up in Section 1 ). When a new edge case appears, it takes editing one SKILL.md; the agent's effective capability grows without the challenges of monolithic prompt engineering.

Three properties of skills make this work:

- They are conditional . Loaded only when their description matches the task.

- They are composable . One skill can call tools from another, or chain downstream, without either knowing about the other (Section 7 develops the composition story in depth).
- They are owned . Each lives in a versioned folder with a clear author, so improvement is distributed rather than bottlenecked through a central platform team.
