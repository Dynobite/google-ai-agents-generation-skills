## Ephemeral Sandboxing and State Management

To safely harness this high-velocity "vibe loop," any skill-generated code must first execute within an ephemeral, network-isolated sandbox. Sub-agents designed to execute untrusted code or invoke tools must run in hardened environments, such as dedicated containers, virtual machines, or kernel-level environments like gVisor.

Crucially, these sandboxes are not merely "prisons" for malicious payloads; they must actively block raw host access and completely reset their state between runs. This ensures that even if a vibe-coded script contains a severe vulnerability or is manipulated into a container escape attempt, the compromised logic cannot persist or impact the underlying host node while the agent safely iterates on its solution.
