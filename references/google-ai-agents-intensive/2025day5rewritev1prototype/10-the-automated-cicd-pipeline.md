## The Automated CI/CD Pipeline

An AI agent is a composite system, comprising not just source code but also prompts, tool definitions, and configuration files. This complexity introduces significant challenges: how do we ensure a change to a prompt doesn't degrade the performance of a tool? How do we test the interplay between all these artifacts before they reach users?

The solution is a CI/CD (Continuous Integration/Continuous Deployment) pipeline. It is more than just an automation script; it's a structured process that helps different people in a team collaborate to manage complexity and ensure quality. It works by testing changes in stages, incrementally building confidence before the agent is released to users.

A robust pipeline is designed as a funnel. It catches errors as early and as cheaply as possible, a practice often called "shifting left." It separates fast, pre-merge checks from more comprehensive, resource-intensive post-merge deployments. This progressive workflow is typically structured into three distinct phases:

1.  Phase 1: Pre-Merge Integration (CI) . The pipeline's first responsibility is to provide rapid feedback to the AI Engineer or Prompt Engineer who has opened a pull request. Triggered automatically, this CI phase acts as a gatekeeper for the main branch. It runs fast checks like unit tests, code linting, and dependency scanning. Crucially, this is the

ideal stage to run the agent quality evaluation suite designed by Prompt Engineers. This provides immediate feedback on whether a change improves or degrades the agent's performance against key scenarios before it is ever merged. By catching issues here, we prevent polluting the main branch. The PR checks configuration template 3  generated with the Agent Starter Pack 1  (ASP) is a practical example of implementing this phase with Cloud Build . 4

2. Phase 2: Post-Merge Validation in Staging (CD) . Once a change passes all CI checksincluding the performance evaluation-and is merged, the focus shifts from code and performance correctness to the operational readiness of the integrated system. The Continuous Deployment (CD) process, often managed by the MLOps Team , packages the agent and deploys it to a staging environment-a high-fidelity replica of production. Here, more comprehensive, resource-intensive tests are run, such as load testing and integration tests against remote services. This is also the critical phase for internal user testing (often called "dogfooding"), where humans within the company can interact with the agent and provide qualitative feedback before it reaches the end user. This ensures that the agent as an integrated system performs reliably and efficiently under productionlike conditions before it is considered for release. The staging deployment template 5  from ASP shows an example of this deployment.
3.  Phase 3: Gated Deployment to Production . After the agent has been thoroughly validated in the staging environment, the final step is deploying to production. This is almost never fully automatic, typically requiring a Product Owner to give the final sign-off, ensuring human-in-the-loop. Upon approval, the exact deployment artifact that was tested and validated in staging is promoted to the production environment. This production deployment template 6  generated with ASP shows how this final phase retrieves the validated artifact and deploys it to production with appropriate safeguards.

Figure 3: Different stages of the CI/CD process

<!-- image -->

Making this three-phase CI/CD workflow possible requires robust automation infrastructure and proper secrets management. This automation is powered by two key technologies:

- Infrastructure as Code (IaC): Tools like Terraform define environments programmatically, ensuring they are identical, repeatable, and version-controlled. For example, this template generated with Agent Starter Pack 7  provides Terraform configurations for complete agent infrastructure including Agent Platform, Cloud Run, and BigQuery resources.
- Automated Testing Frameworks: Frameworks like Pytest execute tests and evaluations at each stage, handling agent-specific artifacts like conversation histories, tool invocation logs, and dynamic reasoning traces.

Furthermore, sensitive information like API keys for tools should be managed securely using a service like Secret Manager 8  and injected into the agent's environment at runtime, rather than being hardcoded in the repository.
