# Reddit Comment Analysis Skill

## Purpose

This skill is used to analyze Reddit comments and automatically discover meaningful categories or industries from the comment data.

The workflow uses text embeddings and clustering to group similar comments without requiring manually labeled training data.

---

## When to Invoke This Skill

Invoke this skill when:

- The input contains Reddit comments or similar user-generated text.
- Comments need to be grouped by topics, industries, or similar patterns.
- The categories are not already known or manually labeled.
- The workflow requires discovering patterns from unlabeled text.
- The output will be used for further analysis, classification, or content generation.

Typical workflow:

1. Load the comment data.
2. Clean and validate the text.
3. Generate sentence embeddings.
4. Cluster similar comments.
5. Inspect and label the discovered clusters.
6. Prepare the resulting data for downstream tasks.

---

## When NOT to Invoke This Skill

Do not invoke this skill when:

- The input is not text/comment data.
- The categories are already fixed and only simple rule-based classification is required.
- The task only requires basic text cleaning.
- The task requires a completely unrelated workflow.
- There is already a reliable supervised classification model and the task only requires making predictions.
- The user only wants a simple summary of a small amount of text.

---

## Input

The skill expects comment data containing text, for example:

- Reddit comments
- Thread comments
- Comment metadata such as client, subreddit, or thread title

---

## Output

The skill produces:

- Grouped comments
- Cluster IDs
- Discovered patterns/topics
- Human-readable cluster labels after inspection

Example:

```text
Cluster 0 → Footwear
Cluster 1 → Dating
Cluster 2 → Home Appliances