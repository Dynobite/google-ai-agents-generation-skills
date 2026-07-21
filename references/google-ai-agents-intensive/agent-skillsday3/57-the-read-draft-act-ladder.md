## The read / draft / act ladder

The second governance decision is what each skill is allowed to do. This is the same tier model from Section 4, applied with retail-specific examples:

| Tier           | Capability                                                  | Review                                                 | Examples                                               |
|----------------|-------------------------------------------------------------|--------------------------------------------------------|--------------------------------------------------------|
| Read-Only      | May fetch, query, or describe data; cannot mutate state     | Domain team approval                                   | review-summarize, store-locator, project-guidance      |
| Draft-Only     | May produce content for human review; cannot send or commit | Domain team + format owner                             | draft-customer-email, materials-list                   |
| Action-Allowed | May execute irreversible operations on real systems         | Domain team + security/compliance + executive sign-off | issue-refund, send-customer-message, reserve-inventory |

T able 6: The read/draft/act governance ladder classifying skill capabilities, review requirements, and operational examples.

This is far more defensible to a security team, and to the regulator who eventually shows up, than the alternative: a black-box agent that does whatever its training plus its system prompt produce.
