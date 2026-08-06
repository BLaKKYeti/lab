# Debug Error

Investigate before making changes.

Steps:

1. Identify the error.
2. Explain the probable cause.
3. Locate affected files.
4. Suggest the smallest safe fix.
5. Explain risks.
6. Apply the fix only after analysis.

After fixing:

Run:

python -m pytest

ruff check .

Summarize:

- root cause
- files changed
- validation performed