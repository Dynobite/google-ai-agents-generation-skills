## Building Security from the Start

Safe deployment strategies protect you from bugs and outages, but agents face a unique challenge: they can reason and act autonomously. A perfectly deployed agent can still cause harm if it hasn't been built with proper security and responsibility measures. This requires a comprehensive governance strategy embedded from day one, not added as an afterthought.

Unlike traditional software that follows predetermined paths, agents make decisions. They interpret ambiguous requests, access multiple tools, and maintain memory across sessions. This autonomy creates distinct risks:

- Prompt Injection &amp; Rogue Actions: Malicious users can trick agents into performing unintended actions or bypassing restrictions.
- Data Leakage: Agents might inadvertently expose sensitive information through their responses or tool usage.
- Memory Poisoning: False information stored in an agent's memory can corrupt all future interactions.

Fortunately, frameworks like Google's Secure AI Agents approach 12  and the Google Secure AI Framework (SAIF) 13  address these challenges through three layers of defense:

1.  Policy Definition and System Instructions (The Agent's Constitution): The process begins by defining policies for desired and undesired agent behavior. These are engineered into System Instructions (SIs) that act as the agent's core constitution.
2. Guardrails, Safeguards, and Filtering (The Enforcement Layer): This layer acts as the hard-stop enforcement mechanism.
- Input Filtering: Use classifiers and services like the Perspective API to analyze prompts and block malicious inputs before they reach the agent.

- Agent Gateway &amp; Output Filtering: After the agent generates a response, Agent Platform's built-in safety filters provide a final check for harmful content, PII, or policy violations. For example, before a response is sent to the user, it is passed through Agent Platform's built-in safety filters 14 , which can be configured to block outputs containing specific PII, toxic language, or other harmful content. Furthermore centralized controls are also needed to ensure safety. For example, before a response is sent to the user, it is passed through the Agent Gateway and Model Armor 14 , providing a final check against harmful content, prompt injection, tool poisoning, and sensitive data leakage.
- Human-in-the-Loop (HITL) Escalation: For high-risk or ambiguous actions, the system must pause and escalate to a human for review and approval.
3.  Continuous Assurance and Testing: Safety is not a one-time setup. It requires constant evaluation and adaptation.
- Rigorous Evaluation: Any change to the model or its safety systems must trigger a full re-run of a comprehensive evaluation pipeline using Agent Platform's evaluation and observability suite .
- Dedicated RAI Testing: Rigorously test for specific risks either by creating dedicated datasets or using simulation agents, including Neutral Point of View (NPOV) evaluations and Parity evaluations .
- Proactive Red Teaming: Actively try to break the safety systems through creative manual testing and AI-driven persona-based simulation .
