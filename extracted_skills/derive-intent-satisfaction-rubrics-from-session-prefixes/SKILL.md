---
name: Derive Intent Satisfaction Rubrics from Session Prefixes
description: Use this skill when evaluating whether an agent's output aligns with the user's original, underspecified intent.
---

You are an expert at AI evaluation. When deriving intent rubrics from a session, follow these steps:

1. Extract the first two user messages from the session to define the 'vibe' or intent.
2. Use an LLM-as-a-judge to generate 3-5 acceptance criteria based on these messages.
3. Score every subsequent agent turn against these criteria using a 1-5 scale.

```python
from google import genai
client = genai.Client(vertexai=True, project="...", location="us-central1")
opening = " ".join(session.user_messages[:2])
criteria = client.models.generate_content(
    model="gemini-3-pro",
    contents=f"Produce 3-5 acceptance criteria for: {opening}. Return JSON.",
).parsed["criteria"]
score = client.models.generate_content(
    model="gemini-3-pro",
    contents=f"Does this output satisfy {criteria}? Score 1-5 with rationale. Output: {agent_response}",
).parsed
```