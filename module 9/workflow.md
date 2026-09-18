# Assignment 9 - Safe AI Coding Workflow

## Objective

Use AI coding tools such as Cursor and Claude Code safely when making changes to a small software repository.

The workflow follows:

Review → Edit → Review Diff → Test → Verify

---

## 1. Review

Before making any changes:

- Understand the repository structure.
- Identify the file that needs to be changed.
- Read the existing code.
- Understand the expected behavior.
- Check the existing tests.

The AI should not make large changes without understanding the existing code.

---

## 2. Edit

Use an AI coding tool such as Cursor or Claude Code to make a small, focused change.

The request should clearly describe:

- What needs to change.
- Which file should be changed.
- What behavior should remain unchanged.

Avoid asking the AI to rewrite the entire repository when a small edit is sufficient.

---

## 3. Review the Diff

After the AI makes a change:

- Review the Git diff.
- Check every modified file.
- Look for unnecessary changes.
- Check for broken or unexpected logic.
- Make sure no secrets, API keys, or sensitive information were added.

Do not accept an AI-generated change blindly.

---

## 4. Test

Run the project's available tests.

If automated tests are not available:

- Run the application.
- Test the changed functionality manually.
- Check for errors.

The change should only be considered successful after testing.

---

## 5. Verify

Compare the result with the original requirement.

Check:

- Does the requested change work?
- Did existing functionality continue to work?
- Were unnecessary files changed?
- Are there any errors or warnings?

If the change is incorrect, revert it and try again.

---

## Cursor and Claude Code

Cursor and Claude Code can both assist with understanding, editing, and testing code.

For this practice assignment, Cursor Web was evaluated for the workflow, but repository-based editing was not performed because the required Cloud Agent/repository access was not available on the current account..

Claude Code is documented as an alternative coding agent, but live testing with Claude Code is not performed because a Claude Code subscription is not available.

No subscription is required for the workflow documentation itself.

---

## Safe Coding Rules

1. Understand before editing.
2. Make small changes.
3. Review the Git diff.
4. Never expose API keys or secrets.
5. Run tests after changes.
6. Verify the final behavior.
7. Revert changes that are incorrect.

## Conclusion

AI coding tools can speed up development, but the developer remains responsible for reviewing and testing the generated changes.

The safest workflow is:

Review → Edit → Diff Review → Test → Verify

## Practical Test Result

A copy of the Module 2 CLI project was used for the experiment so the original assignment remained unchanged.

### Change Made

Added validation for a missing CSV filename.

### Test 1 - Missing Filename

Command:

python app.py ingest

Result:

Please provide a CSV filename

The application exited cleanly without the previous TypeError.

### Test 2 - Normal Input

Command:

python app.py ingest input.csv

Result:

Ingesting file: input.csv
Records loaded: 5

The existing ingest behavior continued to work.

### Result

The change was reviewed before testing and both the new behavior and existing behavior were verified successfully.