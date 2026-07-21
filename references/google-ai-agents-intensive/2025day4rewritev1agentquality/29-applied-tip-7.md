## Applied Tip:

<!-- image -->

Implement your guardrails as a structured Plugin , rather than as isolated functions. In this pattern, the callback is the mechanism (the hook provided by ADK), while the Plugin is the reusable module you build.

For example, you can build a single SafetyPlugin class. This plugin would then register its internal methods with the framework's available callbacks:

1.  Your plugin's check\_input\_safety() method would register with the before\_model\_callback . This method's job is to run your prompt injection classifier.
2.  Your plugin's check\_output\_pii() method would register with the after\_ model\_callback . This method's job is to run your PII scanner.

This plugin architecture makes your guardrails reusable, independently testable, and cleanly layered on top of the foundation model's built-in safety settings (like those in Gemini).
