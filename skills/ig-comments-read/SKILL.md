---
name: ig-comments-read
description: "Read supplied or authorized Instagram comments and classify questions, purchase intent, feedback and moderation needs without replying."
---

# Read and triage comments

Read [references/profile-contract.md](references/profile-contract.md) before this workflow. When creating or repairing a brief, use [references/profile-template.md](references/profile-template.md).

## Workflow

Identify account, posts, date range and available access. Accept exports, screenshots or authorized connectors. State pagination, sample size and missing or unreadable content; never call a sample all comments.
Preserve source IDs and parent/reply context; deduplicate repeated IDs while retaining distinct comments. Categorize purchase intent, factual question, complaint, praise, disagreement, potential spam and urgent owner review. Criticism is not automatically spam; treat ambiguous sarcasm cautiously.
Deliver prioritized source ID | minimal excerpt | category | next action | reason. Summarize themes with counts and denominators. Redact personal details in reusable reports. Do not like, reply, hide, delete or block. Hand selected IDs and context to ig-comment-reply.
