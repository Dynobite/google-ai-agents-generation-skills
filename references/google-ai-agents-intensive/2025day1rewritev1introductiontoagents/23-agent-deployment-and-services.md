## Agent Deployment and Services

After you have built a local agent, you will want to deploy it to a server where it runs all the time and where other people and agents can use it.  Continuing our analogy, deployment and services would be the body and legs for our agent.  An agent requires several services to be effective, session history and memory persistence, and more.  As an agent builder, you will also be responsible for deciding what you log, and what security measures you take for data privacy and data residency and regulation compliance. All of these services are in scope, when deploying agents to production.

Luckily, builders can rely on the newly launched Gemini Enterprise Agent Platform , which provides a single destination for technical teams to build, scale, govern, and optimize agents. This includes the new Agent Studio for seamless transitions from prompting to deployment, and a revamped Agent Runtime delivering sub-second cold starts, support for autonomous multi-day workflows , and Memory Bank for persistent long-term context across sessions, everything else one platform 21 .  For software developers who want to control their application stacks more directly, or deploy agents within their existing DevOps infrastructure, any agent and most agent services can be added to a docker container and deployed onto industry standard runtimes like Cloud Run or GKE 22 .

Figure 4: Gemini Enterprise Agent Platform

<!-- image -->

[https://cloud.google.com/products/gemini-enterprise-agent-platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)

If you are not a software developer and a DevOps expert, the process of deploying your first agent might be daunting.  Many agent frameworks make this easy with a deploy command or a dedicated platform to deploy the agent, and these should be used for early exploration and onboarding.  Ramping up to a secure and production ready environment will usually require a bigger investment of time and application of best practices, including CI/CD and automated testing for your agents 23 .
