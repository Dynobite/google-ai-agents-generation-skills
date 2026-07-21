## What to Evaluate

Vibe coding agent evaluation breaks into seven dimensions, in two groups. User-facing dimensions are what the developer experiences directly. Internal dimensions describe what the agent does invisibly to the user. In addition, Safety and responsible AI is transversal, it intersects multiple dimensions (code vulnerabilities, refusal behaviour, content safety, IP exposure) and has to be evaluated alongside each of them.

Figure 3: Evaluation dimensions for vibe coding agents

<!-- image -->

1.  Intent satisfaction . Did the agent build what the user meant , not just what they said? The hardest dimension to evaluate because the intent is unstated, ambiguous, and often shifts mid-session. Intent satisfaction is what the user ultimately judges the agent on.
2. Functional correctness . Does the code build, run, and pass tests? The floor, not the ceiling. Easy to measure but easy to game: tests can be deleted or mocked to make red turn green without fixing anything.
3.  Visual and behavioural correctness . For agents that produce web apps or UI, the artifact is the rendered output, not the code. Code-level metrics miss the point entirely. The page either looks right and behaves right, or it doesn't.

4. Cost and efficiency . Token spend, wall-clock latency, tool-call count, and iteration count , how many corrections did the user have to issue before the agent converged? An agent that lands the right diff in 1 turn is a different product from one that needs 8 corrections.
5.  Code quality and convention matching . Does the code match the project's idioms, patterns, and conventions? A diff that passes tests but violates the codebase's style is a vibe-coding failure even when locally correct.
6.  Trajectory quality . Did the agent take a sensible path: read the related files first, sequence the edits coherently, pick the right tool or skill at each step? Correct output produced by bad reasoning is a fragile success.
7.  Self-repair behaviour . When the build fails, the test breaks, or the user says "no, not like that," does the agent recover or compound the failure? Recovery quality compounds across a multi-turn session.

These dimensions are not independent. For instance, stronger trajectory quality (dimension 6) tends to mean stronger functional correctness (dimension 2), which is a prerequisite for intent satisfaction (dimension 1).
