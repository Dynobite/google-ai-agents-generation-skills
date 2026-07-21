## Compare against the alternatives:

Table 2: Comparison of agent improvement methodologies across cycle times, failure modes, organizational ownership, and context costs.

| Improvement style   | Cycle time       | Failure mode                         | Who can do it                | Context Tax                               |
|---------------------|------------------|--------------------------------------|------------------------------|-------------------------------------------|
| Model swap          | Days to weeks    | Regression in unrelated tasks        | ML/platform team             | None (weights-based)                      |
| System prompt edit  | Minutes to hours | Context rot, instruction conflict    | Whoever owns the prompt file | Static (every turn pays)                  |
| Fine-tune           | Weeks to months  | Catastrophic forgetting, overfitting | ML team only                 | None (weights-based)                      |
| New skill           | Hours to days    | Bounded with only matching turns     | Any domain team              | Dynamic (loaded on-demand when triggered) |
