# Python scanner worker

This service consumes scan jobs from a queue (e.g. AWS SQS), clones the target GitHub repository into `../workspace/`, runs Python SAST rules, and persists a scan report.

## Local development (placeholder)

- Create a virtual environment and install dependencies (to be added).
- Run the worker entrypoint (to be implemented).

