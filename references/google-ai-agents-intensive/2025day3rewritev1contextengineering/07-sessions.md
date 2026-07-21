## Sessions

A foundational element of Context Engineering is the session, which encapsulates the immediate dialogue history and working memory for a single, continuous conversation. Each session is a self-contained record that is tied to a specific user. The session allows the agent to maintain context and provide coherent responses within the bounds of a single conversation. A user can have multiple sessions, but each one functions as a distinct, disconnected log of a specific interaction. Every session contains two key components: the chronological history ( events ) and the agent's working memory ( state ).

Events are the building blocks of the conversation. Common types of events include: user input (a message from the user (text, audio, image, etc.), agent response (the agent's reply to the user), tool call (the agent's decision to use an external tool or API), or tool output (the data returned from a tool call, which the agent uses to continue its reasoning).

Beyond the chat history, a Session often includes a state -a structured "working memory" or scratchpad. This holds temporary, structured data relevant to the current conversation, like what items are in a shopping cart.

As the conversation progresses, the agent will append additional events to the session. Additionally, it may mutate the state based on logic in the agent.

The structure of the events is analogous to the list of Content objects passed to the Gemini API, where each item with a role and parts represents one turn-or one Event-in the conversation.

```
Python contents = [ { "role": "user", "parts": [ {"text": "What is the capital of France?"} ] }, { "role": "model", "parts": [ {"text": "The capital of France is Paris."} ] } ] response = client.models.generate_content( model="gemini-2.5-flash", contents=contents )
```

Snippet 1: Example multi-turn call to Gemini

A production agent's execution environment is typically stateless, meaning it retains no information after a request is completed. Consequently, its conversation history must be saved to persistent storage to maintain a continuous user experience. While in-memory storage is suitable for development, production applications should leverage robust databases to reliably store and manage sessions. For example, you can store conversation history in managed solutions like Agent Platform Sessions 3  (formerly Agent Builder Sessions) running on the high-performance Agent Runtime . For example, you can store conversation history in managed solutions like Agent Engine Sessions.
