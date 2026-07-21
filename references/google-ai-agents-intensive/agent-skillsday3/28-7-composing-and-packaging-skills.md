## 7. Composing and Packaging Skills

Real workflows do not fit inside a skill. The composition problem is how skills reference each other, pass state, and avoid circular dependencies.

Passing raw LLM outputs between isolated skills in a monolithic system is ineffective: state gets obfuscated, execution becomes non-deterministic, and debugging is hard. Agent architecture has evolved from naive prompt chaining to predictable orchestration.
