## The Agentic Problem-Solving Process

We have defined an AI agent as a complete, goal-oriented application that integrates a reasoning model, actionable tools, and a governing orchestration layer. A short version is 'LMs in a loop with tools to accomplish an objective.'

But how does this system actually work ? What does an agent do from the moment it receives a request to the moment it delivers a result?

At its core, an agent operates on a continuous, cyclical process to achieve its objectives. While this loop can become highly complex, it can be broken down into five fundamental steps as discussed in detail in the book Agentic System Design: 6

1.  Get the Mission: The process is initiated by a specific, high-level goal. This mission is provided by a user (e.g., "Organize my team's travel for the upcoming conference") or an automated trigger (e.g., "A new high-priority customer ticket has arrived").
2. Scan the Scene: The agent perceives its environment to gather context. This involves the orchestration layer accessing its available resources: "What does the user's request say?", "What information is in my term memory? Did I already try to do this task? Did the user give me guidance last week?", "What can I access from my tools, like calendars, databases, or APIs?"
3.  Think It Through: This is the agent's core "think" loop, driven by the reasoning model. The agent analyzes the Mission (Step 1) against the Scene (Step 2) and devises a plan. This isn't a single thought, but often a chain of reasoning: "To book travel, I first need to know who is on the team. I will use the get\_team\_roster tool. Then I will need to check their availability via the calendar\_api ."
4. Take Action: The orchestration layer executes the first concrete step of the plan. It selects and invokes the appropriate tool -calling an API, running a code function, or querying a database. This is the agent acting on the world beyond its own internal reasoning.
5.  Observe and Iterate: The agent observes the outcome of its action. The get\_ team\_roster tool returns a list of five names. This new information is added to the agent's context or "memory." The loop then repeats, returning to Step 3: "Now that I have the roster, my next step is to check the calendar for these five people. I will use the calendar\_api ."

This "Think, Act, Observe" cycle continues - managed by the Orchestration Layer , reasoned by the Model , and executed by the Tools until the agent's internal plan is complete and the initial Mission is achieved.

Figure 1: Agentic AI problem-solving process

<!-- image -->

Let's take a real-world example of how a Customer Support Agent would operate in this 5-step cycle:

Imagine a user asks, "Where is my order #12345?"

Instead of immediately acting, the agent first enters its "Think It Through" phase to devise a complete strategy. It reasons:

- "The user wants a delivery status. To provide a complete answer, I need a multi-step plan:
1.  Identify: I must first find the order in our internal database to confirm it exists and get its details.
2.  Track: From those details, I'll need to extract the shipping carrier's tracking number. Then, I'll query the external carrier's API for the live status.
3.  Report: Finally, I must synthesize the information I've gathered into a clear, helpful response for the user."

With this multi-step plan in mind, the agent begins execution.

In its first "Act" phase, it executes step one of its plan, calling the find\_order("12345") tool. It observes the result-a full order record, including the tracking number "ZYX987."

The agent's orchestration layer recognizes that the first part of its plan is complete and immediately proceeds to the second. It acts by calling the get\_shipping\_ status("ZYX987") tool. It observes the new result: "Out for Delivery."

Finally, having successfully executed the data-gathering stages of its plan, the agent moves to the "Report" step. It perceives it has all the necessary components, plans the final message, and acts by generating the response: "Your order #12345 is 'Out for Delivery'!
