## The failure mode that breaks demos: context overflow

The most common failure mode of agents in production is not hallucination. It is context overflow: the model receiving more context than it can effectively use, and degrading silently before the operator notices. Two strands of research ground this:

Lost in the Middle (Liu et al., TACL 2024 19 ) . Across multi-document QA and retrieval, performance is highest when relevant information sits at the start or end of the input and degrades in the middle; a U-curve that holds even for models trained on long contexts.

Context Rot (Chroma Research, 2025 20 ) . Across 18 frontier models; Claude 4 Opus and Sonnet, Gemini 2.5, Qwen3; performance degrades as input grows, even when task difficulty is held constant. Every model gets worse, and faster when relevant content is hard to distinguish from distractors. The noise typical of real agent contexts (tool outputs, halfrelevant retrievals, intermediate reasoning) is among the worst.

Figure 7: Context rot in practice. As prompt size grows, accuracy on a fixed task degrades, long before the context window fills. The dashed line shows the naive expectation; the curve shows what 18 frontier models actually do (Liu et al. 2024; Chroma 2025).

<!-- image -->
