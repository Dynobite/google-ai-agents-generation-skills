## How does the same query route through the library

Consider what happens when a customer asks: "I want to remodel my kids' bathroom, what do I need?"

The runtime loads the L1 descriptions of all skills at session start (~30 to 80 tokens each, ~2KB total). It identifies that project-guidance matches and loads its body, which produces an outline of the renovation steps. If the customer follows up about delivery, the deliverywindow skill loads. If they ask about returns on a specific item, return-policy loads. The previous skills can stay in context or be released as the conversation moves.

Notice what does not happen. There is no monolithic "remodeling assistant" agent that has been trained on every possible remodeling scenario. Each piece of expertise is loaded into context only when the conversation reaches it. The active context stays small. The available capability is effectively unbounded.
