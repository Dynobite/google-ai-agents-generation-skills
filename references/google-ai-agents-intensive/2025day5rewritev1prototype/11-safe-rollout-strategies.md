## Safe Rollout Strategies

While comprehensive pre-production checks are essential, real-world application inevitably reveals unforeseen issues. Rather than switching 100% of users at once, consider minimizing risk through gradual rollouts with careful monitoring.

Here are four proven patterns that help teams build confidence in their deployments:

- Canary: Start with 1% of users, monitoring for prompt injections and unexpected tool usage. Scale up gradually or roll back instantly.
- Blue-Green: Run two identical production environments. Route traffic to "blue" while deploying to "green," then switch instantly. If issues emerge, switch back-zero downtime, instant recovery.
- A/B Testing: Compare agent versions on real business metrics for data-driven decisions. This can happen either with internal or external users.
- Feature Flags: Deploy code but control release dynamically, testing new capabilities with select users first.

All these strategies share a foundation: rigorous versioning . Every component-code, prompts, model endpoints, tool schemas, memory structures, even evaluation datasetsmust be versioned. When issues arise despite safeguards, this enables instant rollback to a known-good state. See this as your production "undo" button!

You can deploy agents using Agent Runtime 9 or Cloud Run 10 , then leverage Cloud Load Balancing 11  for traffic management across versions or connect to other microservices. The Agent Starter Pack 1  provides ready-to-use templates with GitOps workflows-where every deployment is a git commit, every rollback is a git revert, and your repository becomes the single source of truth for both current state and complete deployment history.
