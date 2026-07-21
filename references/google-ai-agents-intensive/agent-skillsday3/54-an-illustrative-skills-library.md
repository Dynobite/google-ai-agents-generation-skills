## An illustrative skills library

What does that library actually look like? Below is a representative set of skills a major homeimprovement retailer would plausibly maintain. Each is one folder. Each has a single owner. Each has its own eval suite (using the patterns from Section 4). Together, they constitute the company's working memory of how it serves customers.

- project-guidance . Encodes the trades' knowledge that turns a vague query ("how do I tile a shower?") into a step-by-step plan. Includes structural dependencies (substrate must be waterproofed before tiling), ordering logic (cuts before installation), and common-mistake callouts. Owned by the trades knowledge team. Read-only tier.

- materials-list . Takes a project description (voice, text, or partial list) and produces a grouped bill-of-materials, including items the contractor is likely to forget. Owned by Pro merchandising. Draft-only tier: the customer reviews before purchasing.
- review-summarize . Condenses long product reviews into pros, cons, and common use cases. Triggered when the customer asks about real-world experience with a product. Owned by personalization. Read-only tier.
- delivery-window . Computes last-mile delivery options and ETAs given the customer's location, the store's availability, and the company's freight network. Owned by fulfillment. Read-only tier.
- return-policy . Encodes the company's return rules, including the dozens of exceptions for special-order items, hazardous materials, custom cuts, and contract pricing. Owned by customer service. Read-only tier. Promotion to action-allowed (e.g. issuing a refund) requires a second skill with much tighter review.

Each one is small enough to be reviewed, tested, and shipped independently.
