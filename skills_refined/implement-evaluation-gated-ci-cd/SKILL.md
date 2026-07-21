---
name: Implement Evaluation-Gated CI/CD
description: Use this skill when configuring a CI/CD pipeline to ensure agent quality before deployment.
---

You are an expert at MLOps and AgentOps. When tasked with implementing an evaluation-gated pipeline, follow these steps:

1. Define a 'golden dataset' of test cases representing expected agent behavior.
2. Integrate an evaluation harness into the CI phase to run against the golden dataset.
3. Configure the pipeline to block deployment if key metrics (e.g., tool call success rate, helpfulness) fall below defined thresholds.
4. Use Infrastructure as Code (Terraform) to ensure environment parity between staging and production.

Example of a PR check configuration structure:
```yaml
# .cloudbuild/pr_checks.yaml
steps:
  - name: 'python:3.11'
    entrypoint: 'pytest'
    args: ['tests/evaluation_suite.py']
    env:
      - 'EVAL_THRESHOLD=0.9'
```

## Background
- [Evaluation as a Quality Gate](../../references/google-ai-agents-intensive/2025day5rewritev1prototype/09-evaluation-as-a-quality-gate.md)
- [Metrics-Driven Development: Your Go/No-Go for Deployment](../../references/google-ai-agents-intensive/2025day1rewritev1introductiontoagents/27-metrics-driven-development-your-gono-go-for-deployment.md)
- [The Automated CI/CD Pipeline](../../references/google-ai-agents-intensive/2025day5rewritev1prototype/10-the-automated-cicd-pipeline.md)
