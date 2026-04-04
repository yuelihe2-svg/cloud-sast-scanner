# cloud-sast-scanner

A cloud-based source code vulnerability scanner powered by SAST tools and GenAI.

## Project layout

| Path | Role |
|------|------|
| `backend/` | Web API: accept GitHub URLs, orchestrate clone + scan, return/store reports |
| `backend/app/api/routes/` | HTTP endpoints (health, submit scan, fetch report) |
| `backend/app/core/` | Settings, logging, security-related app config |
| `backend/app/models/` | Database or persistence models (optional) |
| `backend/app/schemas/` | Request/response validation (e.g. Pydantic) |
| `backend/app/services/` | GitHub integration, job queue, GenAI report generation |
| `scanner/` | Reusable Python SAST library (rules + engine) |
| `scanner/rules/` | Detectors: SQL injection, XSS, hardcoded secrets, etc. |
| `frontend/` | Web UI: submit repo URL, poll status, display findings |
| `infra/docker/` | Container images and compose for local/cloud deploy |
| `scripts/` | One-off dev/ops helpers |
| `workspace/` | Local-only directory for cloned repositories (gitignored contents) |
