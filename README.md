# cloud-sast-scanner

A cloud-based source code vulnerability scanner powered by SAST tools and GenAI.

## Project layout

**Stack:** Go Backend API (orchestration) · Python Scanner Worker · Vite + React + TypeScript frontend.

| Path | Role |
|------|------|
| `backend/cmd/server/` | `main` package: process entry, wires HTTP server and dependencies |
| `backend/internal/api/` | HTTP handlers and routing (health, scans, reports) |
| `backend/internal/config/` | Configuration loading (env, defaults, secrets) |
| `backend/internal/service/` | Orchestration: validate requests, create job IDs, publish jobs to queue, query status, return report metadata |
| `worker/` | Python scanner worker service (queue consumer) |
| `worker/scanner/` | Reusable Python scanning engine (AST/regex rules) used by the worker |
| `worker/scanner/rules/` | Detectors: SQL injection, XSS, hardcoded secrets, … |
| `frontend/` | Web UI: submit repo URL, poll status, display findings |
| `infra/docker/` | Container images and compose for local/cloud deploy |
| `scripts/` | One-off dev/ops helpers |
| `workspace/` | Local-only directory for cloned repositories (gitignored contents) |

Go module root: `backend/go.mod`; run the API from `backend/` with `go run ./cmd/server`.

The `internal/` layout keeps packages **private to this module** (idiomatic Go).

### Architecture (high level)

- **Go Backend API**: receives requests, validates input, creates a scan job, publishes it to a queue (e.g. SQS), and serves status/result queries.
- **Python Worker**: consumes jobs from the queue, clones the target repo into `workspace/`, runs SAST rules over Python files, stores the report (e.g. S3 / DB), and updates job status.

### Note on `internal/`

Code under `backend/internal/` cannot be imported by other modules—only by packages inside `backend/`. This matches a single-backend monorepo; extract a shared library later only if needed.

### Frontend

Unchanged: `frontend/` uses Vite + React + TypeScript (add `package.json` when scaffolding the UI).
