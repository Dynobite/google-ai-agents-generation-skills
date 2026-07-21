## Background vs. Blocking Operations

Memory generation is an expensive operation requiring LLM calls and database writes. For agents in production, memory generation should almost always be handled asynchronously as a background process 23 .

After an agent sends its response to the user, the memory generation pipeline can run in parallel without blocking the user experience. This decoupling is essential for keeping the agent feeling fast and responsive. A blocking (or synchronous) approach, where the user has to wait for the memory to be written before receiving a response, would create an unacceptably slow and frustrating user experience. This necessitates that memory generation occurs in a service that is architecturally separate from the agent's core runtime.
