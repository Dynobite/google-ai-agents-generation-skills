## Elicitation, MFA Challenges, and the "Vibe Diff"

While automated identity constraints handle the majority of routine tasks, high-stakes actions-such as modifying production databases, executing financial transfers, or altering IAM configurations-require explicit verification and cannot rely on simple "approve/deny" buttons. Because vibe coders often rely on the AI to write complex syntax they may not fully understand (the "It Works, Ship It" fallacy), simple approval gates quickly cause confirmation fatigue, leading developers to blindly authorise code they do not comprehend.

To combat this, the system must implement structured, context-aware elicitation. The agent is forced to actively request confirmation based on the specific context of a high-risk action, which must be accompanied by two distinct security boundaries:

- Cryptographic Hardware MFA: The system should mandate physical multi-factor authentication challenges, such as requiring the developer to touch a hardware USB security key to cryptographically approve the execution.
- The Vibe Diff: Before a critical tool runs, an Evaluator Quorum intercepts the request and translates the complex, generated code back into a plain-English summary. This "Vibe Diff" shows the human developer exactly how their original, fuzzy intent maps to the proposed execution steps, ensuring the human operator actually understands what they are authorising before providing explicit cryptographic consent.

Even with perfect identity verification and granular human authorisation, malicious instructions can still slip past initial defences. When developers blindly trust open-source repositories or pull in massive blocks of unstructured context, they invite sophisticated semantic attacks that bypass standard IAM controls. To proactively detect and neutralise these hidden threats as the code is being generated, security operations must evolve to match the exact speed of the agentic workflow.
