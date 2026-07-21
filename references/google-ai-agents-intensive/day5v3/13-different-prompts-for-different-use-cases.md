## Different Prompts for Different Use Cases

There isn't just one way to turn a spec into code. This can be broken down into several Execution Modes, each requiring a different mindset:

1. Project Generation (The Architect): In this mode, scaffolding is done from scratch-building the skeleton of the project. No YOLO Mode: The agent should be explicitly prompted not to code immediately. It should

propose the folder structure and tech stack first for confirmation. Ensure the prompt includes the generation of tests, documentation and logging (the digital "black box" that records what the app is doing).

Include version numbers for every library. Without them, the agent might suggest an older version of a tool because its "knowledge cutoff"-the date its training data ended-was in the past.
