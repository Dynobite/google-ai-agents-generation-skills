## Discovery

Vibe coders do not write custom connectors; they locate pre-built MCP servers from three primary sources:

- Public MCP Registries: Publicly available registries host hundreds of pre-built servers (e.g., registry.modelcontextprotocol.io , github.com/mcp ). These are excellent for rapid local prototyping but are unvetted and used at your own risk.
- Third-Party (3P) Remote MCP Servers: Vetted platforms expose hosted endpoints. Discover managed pre-vetted MCP servers from official sources. For instance, official Google-published MCP servers (e.g., Google Maps, BigQuery, Google Docs) let your agent securely interact with managed services.
- Internal Registries: Inside an organization, internal tools are exposed as MCP servers and cataloged in a secure registry. The technical implementation of this registry is typically managed via an API gateway, GCP Agent Registry, or a private microservice portal.
