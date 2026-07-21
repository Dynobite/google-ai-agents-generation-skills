## Deploying Agents That Watch Your Repo

You can write a great review prompt. But who runs it on every PR, every nightly sweep without a human pushing the button?

A code review skill runs when you invoke them from inside the IDE. The next step is to deploy them as continuous code analysis agents - services that watch the repository, react to events (PR opened, nightly cron), and post findings back without anyone asking. They catch what tired humans miss on a Friday afternoon: a dependency with a fresh CVE, a TODO from six months ago that quietly became a security gap. Once your team is shipping AI-generated PRs at volume, a continuous reviewer is the only thing that scales with the output. The question is how custom you need to go - and the answer is a spectrum with three tiers, each trading control for simplicity.
