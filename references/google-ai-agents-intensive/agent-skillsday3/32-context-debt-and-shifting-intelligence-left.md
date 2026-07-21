## Context Debt and Shifting Intelligence Left

Skills burn model attention, which is a scarce resource. When authors attempt deterministic behavior at runtime by bloating skill descriptions (e.g., "ALWAYS DO X"), they accumulate Context Debt . Models learn to ignore these capitalized imperatives, exactly as a human developer ignores a wall of unreadable warning text.

The engineering best practice is to Shift Intelligence Left . Instead of hoping an LLM correctly interprets complex rules at runtime, distill subjective judgments into skills. By pushing logic out of the LLM's prompt and into standard, testable scripts, you reduce the chaotic surface area of your application.
