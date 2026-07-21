## What "eval coverage" means

A skill achieves complete eval coverage by satisfying four conditions mapped directly to the primary failure modes:

- Trigger Failure: Verifying trigger behavior with both positive (should fire) and negative (should not fire) test cases.
- Execution Failure: Ensuring correct outputs across a representative range of expected inputs.
- Regression: Confirming that adding the skill causes zero performance drops in the existing library.

- Token Budget Failure: Bounding the skill's token footprint to ensure it does not degrade performance on unrelated turns.

This checklist governs graduation; failure on any single condition holds the skill in the draft tier, regardless of its happy-path performance. Once verified, the skill and its accompanying eval suite are ready for production deployment (detailed in Section 5 ).
