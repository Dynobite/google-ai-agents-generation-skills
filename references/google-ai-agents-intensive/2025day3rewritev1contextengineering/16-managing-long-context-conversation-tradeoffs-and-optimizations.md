## Managing long context conversation: tradeoffs and optimizations

In a simplistic architecture, a session is an immutable log of the conversation between the user and agent. However, as the conversation scales, the conversation's token usage increases. Modern LLMs can handle long contexts, but limitations exist, especially for latency-sensitive applications 10 :

1.  Context Window Limits: Every LLM has a maximum amount of text (context window) it can process at once. If the conversation history exceeds this limit, the API call will fail.
2. API Costs ($): Most LLM providers charge based on the number of tokens you send and receive. Shorter histories mean fewer tokens and lower costs per turn.

3.  Latency (Speed): Sending more text to the model takes longer to process, resulting in a slower response time for the user. The revamped Agent Runtime directly addresses this concern, delivering sub-second cold starts and provisioning new stateful agent instances in seconds, significantly reducing the system overhead added by session restoration. Compaction keeps the agent feeling quick and responsive.
4. Quality: As the number of tokens increases, performance can get worse due to additional noise in the context and autoregressive errors.

Managing a long conversation with an agent can be compared to a savvy traveler packing a suitcase for a long trip. The suitcase represents the agent's limited context window, and the clothes and items are the pieces of information from the conversation. If you simply try to stuff everything in, the suitcase becomes too heavy and disorganized, making it difficult to find what you need quickly-like how an overloaded context window increases processing costs and slows down response times. On the other hand, if you pack too little, you risk leaving behind essential items like a passport or a warm coat, compromising the entire triplike how an agent could lose critical context, leading to irrelevant or incorrect answers. Both the traveler and the agent operate under a similar constraint: success hinges not on how much you can carry, but on carrying only what you need.

Compaction strategies shrink long conversation histories, condensing dialogue to fit within the model's context window, reducing API costs and latency. As a conversation gets longer, the history sent to the model with each turn can become too large. Compaction strategies solve this by intelligently trimming the history while trying to preserve the most important context.

So, how do you know what content to throw out of a Session without losing valuable information? Strategies range from simple truncation to sophisticated compaction:

- Keep the last N turns: This is the simplest strategy. The agent only keeps the most recent N turns of the conversation (a 'sliding window') and discards everything older.
- Token-Based Truncation: Before sending the history to the model, the agent counts the tokens in the messages, starting with the most recent and working backward. It includes as many messages as possible without exceeding a predefined token limit (e.g., 4000 tokens). Everything older is simply cut off.
- Recursive Summarization: Older parts of the conversation are replaced by an AIgenerated summary. As the conversation grows, the agent periodically uses another LLM call to summarize the oldest messages. This summary is then used as a condensed form of the history, often prefixed to the more recent, verbatim messages.

For example, you can keep the last N turns with ADK by using a built-in plug-in for your ADK app to limit the context sent to the model. This does not modify the historical events stored in your session storage:

```
Python
```

Snippet 3: Session truncation to only use the last N turns with ADK

```
from google.adk.apps import App from google.adk.plugins.context_filter_plugin import ContextFilterPlugin app = App( name='hello_world_app', root_agent=agent, plugins=[ # Keep the last 10 turns and the most recent user query. ContextFilterPlugin(num_invocations_to_keep=10), ], )
```

Given that sophisticated compaction strategies aim to reduce cost and latency, it is critical to perform expensive operations (like recursive summarization) asynchronously in the background and persist the results. 'In the background' ensures the client is not kept waiting, and 'persistence' ensures that expensive computations are not excessively repeated. Frequently, the agent's memory manager is responsible for both generating and persisting these recursive summaries. The agent must also keep a record of which events are included in the compacted summary; this prevents the original, more verbose events from being needlessly sent to the LLM.

Additionally, the agent must decide when compaction is necessary. The trigger mechanism generally falls into a few distinct categories:

- Count-Based Triggers (i.e. token size or turn count threshold): The conversation is compacted once the conversation exceeds a certain predefined threshold. This approach is often 'good enough" for managing context length.
- Time-Based Triggers: Compaction is triggered not by the size of the conversation, but by a lack of activity. If a user stops interacting for a set period (e.g., 15 or 30 minutes), the system can run a compaction job in the background.
- Event-Based Triggers (i.e. Semantic/Task Completion): The agent decides to trigger compaction when it detects that a specific task, sub-goal, or topic of conversation has concluded.

For example, you can use ADK's EventsCompactionConfig to trigger LLM-based summarization after a configured number of turns:

```
Python from google.adk.apps import App from google.adk.apps.app import EventsCompactionConfig app = App( name='hello_world_app', root_agent=agent, events_compaction_config=EventsCompactionConfig( compaction_interval=5, overlap_size=1, ), )
```

Snippet 4: Session compaction using summarization with ADK

Memory generation is the broad capability of extracting persistent knowledge from a verbose and noisy data source. In this section, we covered a primary example of extracting information from conversation history: session compaction. Compaction distills the verbatim transcript of an entire conversation, extracting key facts and summaries while discarding conversational filler.

Building on compaction, the next section will explore memory generation and management more broadly. We will discuss the various ways memories can be created, stored, and retrieved to build an agent's long-term knowledge.
