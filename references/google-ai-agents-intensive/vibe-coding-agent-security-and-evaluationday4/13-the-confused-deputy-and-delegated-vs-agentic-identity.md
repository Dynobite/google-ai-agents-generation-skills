## The Confused Deputy and Delegated vs. Agentic Identity

Even with a unique identity, a vibe-coded agent remains highly susceptible to the Confused Deputy problem. This occurs when a prompt injection-such as a malicious instruction hidden inside an open-source repository that a developer unknowingly pasted into their IDE's context window-tricks an over-privileged agent into executing an unauthorised command on the attacker's behalf.

To resolve this, an agent must never be the final arbiter of access. Instead of operating under the human user's delegated credentials, which grants the agent dangerous ambient access, the agent must authenticate using a dedicated identity explicitly tagged as agentic. A distinct, observable agentic identity ensures that its permissions remain strictly bound and subject to granular audit logs.
