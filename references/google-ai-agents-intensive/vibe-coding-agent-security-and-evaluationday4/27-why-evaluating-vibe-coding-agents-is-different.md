## Why evaluating vibe coding agents is different

Evaluating vibe coding agents is not the same problem as evaluating deterministic software, and it's not the same problem as evaluating a customer-service agent or a research agent either.

Three things make it unique:

- The Underspecification Gap (There is no spec) . Traditional software testing operates on the unyielding assumption that a complete, rigid specification exists before a single line of code is evaluated. Vibe coding is the exact opposite: the user's natural language prompt is inherently underspecified. "Make the dashboard load faster" is not a test case. The prompt relies entirely on the foundation model's latent knowledge, aesthetic judgment, and domain expertise to fill in the operational gaps. The first job of evaluation is to determine whether the agent successfully bridged this gap and reconstructed the right unstated spec.
- The user often cannot validate the output . Non-technical users cannot review 600 lines of code line by line. Experienced engineers cannot either, in real time. The gap between "the agent thinks it succeeded" and "the code is actually correct" is wider here than in any other agent category, and closing that gap is the central work of evaluation.
- The session is iterative and the codebase is state . Each turn modifies real files. Bad early decisions compound. Evaluation has to cover not just turn-level decisions but the full arc of a multi-turn conversation, on a living codebase with its own conventions, dependencies, and history.

These three constraints shape every dimension, method, and tip that follows.
