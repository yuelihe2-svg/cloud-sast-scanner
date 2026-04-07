"""
Queue consumer entrypoint (to be implemented).

Target architecture:
- Poll SQS (or another queue) for scan jobs
- Clone repo into ../workspace/<job-id>/
- Run scanner over Python files
- Persist results (S3/DB) and update job status
"""


def main() -> None:
    raise SystemExit("worker entrypoint not implemented yet")


if __name__ == "__main__":
    main()

