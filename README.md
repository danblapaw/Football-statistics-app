# Football Statistics App

A professional platform for football (soccer) statistics, analytics, and insights.

---

## Vision

Build a scalable, data-driven football statistics platform that aggregates match data, player performance, and team analytics across multiple leagues and seasons. The platform will serve both an internal data pipeline and a consumer-facing mobile app.

---

## Tech Stack

| Layer       | Technology                        |
|-------------|-----------------------------------|
| Backend     | Python 3.12 + FastAPI             |
| Database    | PostgreSQL + SQLAlchemy + Alembic |
| Mobile      | Expo React Native (TypeScript)    |
| Data        | Custom ETL scripts (Python)       |
| Infra       | GitHub Codespaces / Railway       |
| AI tooling  | Claude Code (remote control)      |

---

## Project Structure

```
football-statistics-app/
│
├── backend/                   # FastAPI application
│   ├── app/
│   │   ├── main.py            # App entry point
│   │   ├── api/               # Route handlers
│   │   ├── models/            # SQLAlchemy models
│   │   ├── services/          # Business logic
│   │   └── database/          # DB session and config
│   ├── migrations/            # Alembic migrations
│   │   └── versions/          # Migration files
│   ├── alembic.ini
│   ├── requirements.txt
│   └── .env.example
│   └── app/
│       ├── api/               # Route handlers (leagues, teams, players, matches)
│       ├── schemas/           # Pydantic request/response schemas
│       ├── services/          # Business logic (DB queries)
│
├── apps/
│   └── mobile/                # Expo React Native app (Phase 4)
│
├── data/
│   ├── raw/                   # Source data (CSV, JSON, API dumps)
│   ├── clean/                 # Processed, normalized data
│   └── scripts/               # ETL scripts
│
└── docs/
    ├── roadmap.md             # Development phases
    ├── database-schema.md     # Table definitions
    └── api-plan.md            # REST endpoint plan
```

---

## Roadmap

| Phase | Focus                              | Status      |
|-------|------------------------------------|-------------|
| 1     | Project foundation & structure     | Done        |
| 1.5   | Schemas, REST endpoints & services | Done        |
| 2     | Data pipeline & ETL                | Planned     |
| 3     | Statistics engine & REST API       | Planned     |
| 4     | Expo mobile app                    | Planned     |
| 5     | Production deployment & CI/CD      | Planned     |

See [`docs/roadmap.md`](docs/roadmap.md) for details.

---

## Running the Backend

### Prerequisites
- Python 3.12+
- PostgreSQL running locally (or via Docker)

### Setup

```bash
# 1. Create virtual environment
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env and set DATABASE_URL=postgresql://user:password@localhost:5432/football_stats

# 4. Apply database migrations
alembic upgrade head

# 5. Start the API server
uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`.
Interactive docs: `http://localhost:8000/docs`

---

## Database Migrations (Alembic)

All migrations live in `backend/migrations/versions/`. Run every command from the `backend/` directory with the virtual environment active.

```bash
# Apply all pending migrations
alembic upgrade head

# Roll back the last migration
alembic downgrade -1

# Show current applied revision
alembic current

# Show full migration history
alembic history --verbose

# Generate a new migration from model changes
alembic revision --autogenerate -m "describe your change"
```

> **Note:** `DATABASE_URL` must be set in `backend/.env` before running any Alembic command.

---

## REST API Endpoints

All endpoints are prefixed with `/api`. Interactive docs at `/docs`.

| Method | Path                   | Query params                             |
|--------|------------------------|------------------------------------------|
| GET    | /api/leagues           | `skip`, `limit`                          |
| GET    | /api/leagues/{id}      |                                          |
| GET    | /api/teams             | `skip`, `limit`, `league_id`             |
| GET    | /api/teams/{id}        |                                          |
| GET    | /api/players           | `skip`, `limit`, `team_id`               |
| GET    | /api/players/{id}      |                                          |
| GET    | /api/matches           | `skip`, `limit`, `league_id`, `status`   |
| GET    | /api/matches/{id}      |                                          |

See [`docs/api-plan.md`](docs/api-plan.md) for the full plan.

---

## GitHub Codespaces

This project is ready for Codespaces. Open it directly from GitHub and the environment will be pre-configured. A `devcontainer.json` will be added in a future phase.

---

## Contributing

Built with Claude Code. All AI-assisted changes go through pull requests on the `main` branch.
