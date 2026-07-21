## Level 2: The Strategic Problem-Solver

Level 2 marks a significant expansion in capability, moving from executing simple tasks to strategically planning complex, multi-part goals. The key skill that emerges here is context engineering : the agent's ability to actively select, package, and manage the most relevant information for each step of its plan.

An agent's accuracy depends on a focused, high-quality context. Context engineering curates the model's limited attention to prevent overload and ensure efficient performance.

For instance, consider the "Mission": "Find a good coffee shop halfway between my office at 1600 Amphitheatre Parkway, Mountain View, and my client's office at 1 Market St, San Francisco."

A Level 2 agent will start creating a plan:

1.  Think: "I must first find the halfway point."
- Act: Call the Maps tool with both addresses.
- Observe: "The halfway point is Millbrae, CA."
2. Think: "Now I must find coffee shops in Millbrae. The user asked for 'good' ones, so I will search for places with a 4-star rating or higher."

- Act: Call the google\_places tool with query="coffee shop in Millbrae, CA", min\_rating=4.0 . (This is context engineering - it automatically created a new, focused search query from the previous step's output ).
- Observe: "The search returns 'Millbrae Coffee' and 'The Daily Grind'."
3.  Think: "I will synthesize these results and present them to the user."

This strategic planning also enables proactive assistance, like an agent that reads a long flight confirmation email, engineers the key context (flight number, date), and acts by adding it to your calendar.
