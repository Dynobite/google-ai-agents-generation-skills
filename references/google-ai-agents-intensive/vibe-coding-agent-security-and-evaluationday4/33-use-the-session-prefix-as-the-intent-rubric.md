## Use the session prefix as the intent rubric

Vibe coding has no spec to test against, the user's intent, is unstated and evolves across turns. The closest thing to a spec is the first one or two user messages. Treat them as the rubric: derive evaluation criteria automatically from the session prefix, then score every subsequent turn against them. This is the only practical way to evaluate dimension 1 (intent satisfaction) at scale.

```
Python from google import genai client = genai.Client(vertexai=True, project="...", location="us-central1") # Derive criteria from the user's opening turns opening = " ".join(session.user_messages[:2]) criteria = client.models.generate_content( model="gemini-3-pro", contents=f"Produce 3-5 acceptance criteria for: {opening}. Return JSON.", ).parsed["criteria"] # Score every agent turn against the derived criteria score = client.models.generate_content( model="gemini-3-pro", contents=f"Does this output satisfy {criteria}? Score 1-5 with rationale." f"Output: {agent_response}", ).parsed
```

S nippet 1: Deriving intent satisfaction acceptance criteria from a session prefix.
