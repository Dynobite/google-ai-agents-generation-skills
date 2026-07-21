## Connecting Remote A2A Agents

In a mature ecosystem, an application does not natively possess deep knowledge of every domain it touches. Instead, it acts as an Orchestrator -a central hub whose primary cognitive load is dedicated to understanding user intent, managing the overarching workflow, and delegating specific tasks to specialized, remote A2A agents.

Remote A2A agents operate as an autonomous, domain-bound contractor which communicates over the A2A protocol. Connecting to these remote agents generally follows one of two architectural patterns (code sample from Google ADK): direct point-to-point integration:

```
Python # 1. Direct Instantiation via Hardcoded Endpoint # Ideal for specific vendor integrations or private agents billing_specialist = RemoteA2aAgent( name="billing_agent", endpoint="https://api.vendor.com/v1/billing/a2a" )
```

Snippet 2: Direct remote A2A agent instantiation via a hardcoded endpoint.

or by using agent registry to discover agents:

```
Python # 2. InDirect Instantiation via Agent Registry registry = AgentRegistry(project_id=project_id, location=location) #The registry resolves resource names and handles authentication validation agent_name = f"projects/{project_id}/locations/{location}/agents/YOUR_AGENT_ID" my_remote_agent = registry.get_remote_a2a_agent(agent_name=agent_name)
```

Snippet 3: Indirect remote A2A agent discovery and instantiation via an Agent Registry.
