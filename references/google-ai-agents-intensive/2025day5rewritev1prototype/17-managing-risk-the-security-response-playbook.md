## Managing Risk: The Security Response Playbook

Because an agent can act on its own, you need a playbook for rapid containment. When a threat is detected, the response should follow a clear sequence: contain, triage, and resolve .

The first step is immediate containment . The priority is to stop the harm, typically with a "circuit breaker"-a feature flag to instantly disable the affected tool.

Next is triage . With the threat contained, suspicious requests are routed to a human-in-theloop (HITL) review queue to investigate the exploit's scope and impact.

Finally, the focus shifts to a permanent resolution . The team develops a patch-like an updated input filter or system prompt-and deploys it through the automated CI/CD pipeline, ensuring the fix is fully tested before blocking the exploit for good.
