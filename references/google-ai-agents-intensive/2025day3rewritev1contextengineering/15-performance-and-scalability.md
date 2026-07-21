## Performance and Scalability

Session data is on the "hot path" of every user interaction, making its performance a primary concern. Reading and writing the session history must be extremely fast to ensure a responsive user experience. Agent runtimes are typically stateless, so the entire session history is retrieved from a central database at the start of every turn, incurring network transfer latency.

To mitigate latency, it is crucial to reduce the size of the data transferred. A key optimization is to filter or compact the session history before sending it to the agent. For example, you can remove old, irrelevant function call outputs that are no longer needed for the current state of the conversation. The following section details several strategies for compacting history to effectively manage long-context conversations.
