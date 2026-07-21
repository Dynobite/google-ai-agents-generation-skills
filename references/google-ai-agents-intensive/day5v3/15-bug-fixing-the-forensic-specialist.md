## Bug Fixing (The Forensic Specialist)

When things break, forensic mode is required. The goal is root cause analysis and a surgical repair. Shift from Symptom Prompting ("The button doesn't work") to Evidence Prompting ("Logs pulled using gcloud logging read 'textPayload:ERROR' --limit 5 showed a 403 error"). Use versioning on the command line (e.g. gh commands for Git) to compare versions of code. Then explain the flow: "Request hits Load Balancer -&gt; Auth strips header -&gt; Pod fails."
