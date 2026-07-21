## The Anatomy of a Critical Log Entry

To reconstruct an agent's "thought process," a log must be rich with context. A structured JSON format is the gold standard.

- Core Information: A good log captures the full context: prompt/response pairs, intermediate reasoning steps (the agent's "chain of thought", a concept explored by Wei et al. (2022)), structured tool calls (inputs, outputs, errors), and any changes to the agent's internal state.

- The Tradeoff: Verbosity vs. Performance: A highly detailed DEBUG log is a developer's best friend for troubleshooting but can be too "noisy" and create performance overhead in a production environment. This is why structured logging is so powerful; it allows you to collect detailed data but filter it efficiently.

Here's a practical example showing the power of a structured log, adapted from an ADK DEBUG output:

```
JSON // A structured log entry capturing a single LLM request ... 2025-07-10 15:26:13,778 - DEBUG - google_adk.google.adk.models.google_llm - Sending out request, model: gemini-2.0-flash, backend: GoogleLLMVariant.GEMINI_API, stream: False 2025-07-10 15:26:13,778 - DEBUG - google_adk.google.adk.models.google_llm -LLM Request: -----------------------------------------------------------System Instruction: You roll dice and answer questions about the outcome of the dice rolls..... The description about you is "hello world agent that can roll a dice of 8 sides and check prime numbers." -----------------------------------------------------------Contents: {"parts":[{"text":"Roll a 6 sided dice"}],"role":"user"} {"parts":[{"function_call":{"args":{"sides":6},"name":"roll_die"}}],"role":"model"} {"parts":[{"function_response":{"name":"roll_die","response":{"result":2}}}],"role":"user"} -----------------------------------------------------------Functions: roll_die: {'sides': {'type': <Type.INTEGER: 'INTEGER'>}} check_prime: {'nums': {'items': {'type': <Type.INTEGER: 'INTEGER'>}, 'type': <Type.ARRAY: 'ARRAY'>}} -----------------------------------------------------------2025-07-10 15:26:13,779 - INFO - google_genai.models - AFC is enabled with max remote calls: 10. 2025-07-10 15:26:14,309 - INFO - google_adk.google.adk.models.google_llm -LLM Response: -----------------------------------------------------------Text: I have rolled a 6 sided die, and the result is 2. ...
```

Snippet 1: A structured log entry capturing a single LLM request
