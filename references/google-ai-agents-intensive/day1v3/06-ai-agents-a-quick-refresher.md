## AI Agents: A Quick Refresher

An AI agent is a software system that perceives a goal, plans steps to reach it, takes actions through tools, observes the results, and iterates until the goal is met or it hits a stopping condition. Where a chatbot produces a response and waits for the next prompt, an agent runs its own loop. You give it a goal at the top, then it decides what to do next at each step.

Figure 2: The Agent Loop - Perceive, plan, act, observe, iterate.

<!-- image -->

Every agent, however simple or sophisticated, is built from five parts. The November 2025 Introduction to Agents whitepaper covers each in depth.² For our purposes here, the short version:

- The model is the reasoning engine. It reads the current context, decides what should happen next, and produces the next thought, the next tool call, or the next message.
- Tools connect the model to the world. They include APIs the agent can call, code it can execute, databases it can query, and other agents it can delegate to.
- Memory is the state. It allows the agent to recall past interactions, retrieve projectspecific rules, and retain context across sessions so it never starts from a blank slate.
- Orchestration is the code that runs the loop. It assembles the context for each model call, dispatches tool calls, captures their results, and decides whether to continue.
- Deployment is what turns the prototype into a service: hosting, identity, observability, and the production infrastructure the agent runs on.

These four parts work together in a continuous loop: get the mission, scan the scene, think it through, take action, observe and iterate. The loop is the beating heart of every agent. Everything else in this paper, and everything in the rest of the course, is a variation on this loop.
