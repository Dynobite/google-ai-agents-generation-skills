## What the architecture looks like

<!-- image -->

Figure 11. A skills-first retail architecture (illustrative). Customer surfaces (web chat, mobile app, in-store kiosk, voice agent) sit above an agent runtime that loads skills carrying merchandising, category, and compliance knowledge. The tools below are accessed via MCP and managed search integrations.

The architecture has three layers. The top layer is the customer surface: chat on the website, the mobile app, an in-store kiosk, a voice agent in the call center. Each surface is thin. It forwards user input to the runtime and renders the response.

The middle layer is the agent runtime and the orchestrator that maintains the conversation, loads skills, calls tools, and assembles the reply.

The bottom layer is the data and tools plane: the product catalog (often millions of SKUs), live inventory with store-level location data, customer profile and order history, the project knowledge base, and vector search over reviews, manuals, and specification sheets.

What matters for this whitepaper is the middle layer. The runtime itself is generic: Google's Agent Development Kit, Anthropic's Claude Agent SDK, or any of the other runtimes that support the open Skills standard. The skills loaded into that runtime are specific to the retailer's domain, and they are what carry the brand's expertise to the customer.
