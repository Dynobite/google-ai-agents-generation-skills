## The "Outside-In" View: End-to-End Evaluation (The Black Box)

Figure 3: A Framework for Holistic Agent Evaluation

<!-- image -->

The first and most important question is: "Did the agent achieve the user's goal effectively?"

This is the "Outside-In" view. Before analyzing a single internal thought or tool call, we must evaluate the agent's final performance against its defined objective.

Metrics at this stage focus on overall task completion. We measure:

- Task Success Rate: A binary (or graded) score of whether the final output was correct, complete, and solved the user's actual problem, e.g. PR acceptance rate for a coding agent, successful database transaction rate for a financial agent, or session completion rate for a customer service bot.

- User Satisfaction: For interactive agents, this can be a direct user feedback score (e.g., thumbs up/down) or a Customer Satisfaction Score (CSAT).
- Overall Quality: If the agent's goal was quantitative (e.g., "summarize these 10 articles"), the metric might be accuracy or completeness (e.g., "Did it summarize all 10?").

If the agent scores 100% at this stage, our work may be done. But in a complex system, it rarely will. When the agent produces a flawed final output, abandons a task, or fails to converge on a solution, the "Outside-In" view tells us what went wrong. Now we must open the box to see why .

<!-- image -->
