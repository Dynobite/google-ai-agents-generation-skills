## The Evaluation Toolkit

Five complementary testing patterns cover the full failure surface.

| Pattern               | Description                                                             | Example                                                                                                               | Failure Mode Addressed   | When Required                      |
|-----------------------|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------------|
| Eval-as-Unit-Test     | Test file for the skill running in CI on every change                   | Three JSON eval cases run via agenteval on every push; a failing test blocks merges                                   | All                      | Every skill, every change          |
| Golden Dataset        | Curated, versioned (input, expected output) pairs stored with the skill | 30 representative queries with expected tool calls/formats committed in the skill directory                           | Execution, Trigger       | Draft tier and above               |
| LLM-as-Judge          | A peer model evaluates output against a rubric at scale                 | Reference-guided scoring across three rubric dimensions, run twice with swapped positions to neutralize ordering bias | Execution                | Read-only and draft                |
| dversarial / Red-Team | Systematic probing designed to expose failure modes                     | One rephrasing and one negative boundary case for every positive trigger; agentregress flags regressions              | Trigger, Execution       | Before action -alllowed graduation |
| Canary / Shadow Mode  | Deployment to controlled traffic before full rollout                    | Shadow: Parallel offline comparison. Canary: 1% live traffic monitored via selftune for 24 hours                      | Regression               | Before each action-allowed release |

Table 1: The Evaluation Toolkit, outlining five complementary testing patterns designed to cover the full failure surface of Agent Skills.

Figure 2: This visual highlights the gatekeeping mechanism. The metadata acts as a thin routing layer, keeping the active token count low until the specific activation cues match the user intent.

<!-- image -->
