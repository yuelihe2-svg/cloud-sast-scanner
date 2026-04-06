# cloud-sast-scanner

A cloud-based source code vulnerability scanner powered by SAST tools and GenAI.

## Project layout

**Stack:** Go API server · Vite + React + TypeScript frontend.

| Path | Role |
|------|------|
| `backend/cmd/server/` | `main` package: process entry, wires HTTP server and dependencies |
| `backend/internal/api/` | HTTP handlers and routing (health, scans, reports) |
| `backend/internal/config/` | Configuration loading (env, defaults, secrets) |
| `backend/internal/service/` | Orchestration: clone repos, run scans, optional GenAI |
| `backend/internal/scanner/` | SAST engine over Python files under a repo root |
| `backend/internal/scanner/rules/` | Rule implementations (SQLi, XSS, hardcoded secrets, …) |
| `frontend/` | Web UI: submit repo URL, poll status, display findings |
| `infra/docker/` | Container images and compose for local/cloud deploy |
| `scripts/` | One-off dev/ops helpers |
| `workspace/` | Local-only directory for cloned repositories (gitignored contents) |

Go module root: `backend/go.mod`; run the API from `backend/` with `go run ./cmd/server`.

The `internal/` layout keeps packages **private to this module** (idiomatic Go).

### Note on `internal/`

Code under `backend/internal/` cannot be imported by other modules—only by packages inside `backend/`. This matches a single-backend monorepo; extract a shared library later only if needed.

### Frontend

Unchanged: `frontend/` uses Vite + React + TypeScript (add `package.json` when scaffolding the UI).
