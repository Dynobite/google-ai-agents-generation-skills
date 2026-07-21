## Security and Privacy

Protecting the sensitive information contained within a session is a non-negotiable requirement. Strict Isolation is the most critical security principle. A session is owned by a single user, and the system must enforce strict isolation to ensure one user can never access another user's session data (i.e. via ACLs). Every request to the session store must be authenticated and authorized against the session's owner.

A best practice for handling Personally Identifiable Information (PII) is to redact it before the session data is ever written to storage. This is a fundamental security measure that drastically reduces the risk and "blast radius" of a potential data breach. By ensuring sensitive data is never persisted using tools like Model Armor 9 , you simplify compliance with privacy regulations like GDPR and CCPA and build user trust.
