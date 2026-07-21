## Agent Identity: A New Class of Principal

In the traditional security model, there are human users which might use OAuth or SSO, and there are services which use IAM or service accounts. Agents add a 3rd category of principle. An agent is not merely a piece of code; it is an autonomous actor, a new kind of principal that requires its own verifiable identity. Just as employees are issued an ID badge, each agent on the platform must be issued a secure, verifiable "digital passport." This Agent Identity is distinct from the identity of the user who invoked it and the developer who built it. This is a fundamental shift in how we must approach Identity and Access Management (IAM) in the enterprise.

Having each identity be verified and having access controls for all of them, is the bedrock of agent security. Once an agent has a cryptographically verifiable identity (often using standards like SPIFFE 35 ), it can be granted its own specific, least-privilege permissions. The SalesAgent is granted read/write access to the CRM, while the HRonboardingAgent is explicitly denied. This granular control is critical. It ensures that even if a single agent is compromised or behaves unexpectedly, the potential blast radius is contained. Without an agent identity construct, agents cannot work on behalf of humans with limited delegated authority. The Gemini Enterprise Agent Platform now also natively enforces this via the Agent Identity feature, ensuring every agent receives a unique cryptographic ID. This creates a clear, auditable trail mapped back to defined enterprise authorization policies.

Table 1: A non-exhaustive example of different categories of actors for authentication

| Principal entity                     | Authentication / Verification   | Notes                                                                        |
|--------------------------------------|---------------------------------|------------------------------------------------------------------------------|
| Users                                | Authenticated with OAuth or SSO | Human actors with full autonomy and responsibility for their actions         |
| Agents (new category of principles ) | Verified with SPIFFE            | Agents have delegated authority, taking actions on behalf of users           |
| Service accounts                     | Integrated into IAM             | Applications and containers, fully deterministic, no responsible for actions |
