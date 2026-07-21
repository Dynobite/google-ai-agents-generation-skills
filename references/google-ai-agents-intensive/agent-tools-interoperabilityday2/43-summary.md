## Summary

Generative UI lets LLMs create user interfaces at runtime based on user intent. A2UI is Google's open-source standard for doing this safely: a framework-agnostic format for declaring UI intent, so the same agent message renders natively in Lit, Flutter, React, or your own design system.

The security model matters: agents can't inject arbitrary code. They can only request components the renderer's catalog already trusts. That's what makes A2UI safe while still enabling dynamic, generative interfaces.
