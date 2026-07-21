## AP2 (Agent Payments Protocol): The Parent's Credit Card with Strict Rules

Now the food is in the cart, but your AI needs to pay. You obviously aren't going to type your actual debit card number into an AI prompt and say "Go wild."

AP2 is the open, shared protocol that provides a common language for secure, compliant transactions between agents and merchants that lets your AI pay for the food only within rules you set.

- The Guardrails (The Mandate): Before you send the AI off, you approve a digital rule: "You can spend up to $25 at Taco Bell."
- The Handshake: When the AI checks out, it doesn't show your card number. It shows a digital, encrypted "promissory note" signed by you that says: "My human approved this $18.50 order." The restaurant's bank instantly verifies this digital signature.
- No Hidden Fees: If the restaurant tries to sneakily charge you $50 instead of $18.50, the AP2 protocol blocks it instantly because it violates the rules you signed off on.

In short: AP2 is the secure lockbox that lets your AI pay for things using your money, but ensures it can never buy a $1,000 TV by mistake.

Table 3: Comparison for UCP and AP2

| UCP                                                                                   | AP2                                                                                              |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Brain that decides what to buy, handles the menu, and puts the food in the cart.      | Is the wallet that securely handles how to pay for it without you getting scammed.               |
| Integrates with any business provider                                                 | Integrates with payment                                                                          |
| Unified integration: Shared language: Extensible architecture Security-first approach | Authorization & Auditability Authenticity of Intent Agent Error and Hallucination Accountability |

- If you are a developer building your UCP agent  for a merchant or the payment processor, follow the instructions here .
- If you are a developer building your AP2 agent for a merchant or the payment processor, follow the instructions here .
- If you are a developer building an agent that consumes an AP2 agent such as a shopper, follow the instructions here .
