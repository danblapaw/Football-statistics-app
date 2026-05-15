# Roadmap

> **MVP scope:** Season **2025-2026** only. No historical data will be loaded.

## Phase 1 — Foundation (Done)
- [x] Project structure and repository setup
- [x] FastAPI backend skeleton with CORS
- [x] PostgreSQL schema design
- [x] Core data models: League, Team, Player, Match, PlayerStats
- [x] Alembic migrations configured (revision 0001)

## Phase 1.5 — API Layer (Done)
- [x] Pydantic schemas (Base / Create / Read) for all entities
- [x] Service layer with SQLAlchemy 2.0 select() queries
- [x] REST endpoints: leagues, teams, players, matches
- [x] Pagination (`skip` / `limit`) on all list endpoints
- [x] `season` filter on all list endpoints (default: 2025-2026)
- [x] `season` column added to Match and PlayerStats models (revision 0002)
- [x] `ACTIVE_SEASON = "2025-2026"` constant propagated across models, schemas, and routers

## Phase 2 — Data Pipeline
- [ ] Data ingestion scripts (external football APIs or CSV)
- [ ] ETL pipeline: raw → clean → database (season 2025-2026 only)
- [ ] Seed script for leagues and teams

## Phase 3 — Statistics Engine
- [ ] Per-match stat aggregation
- [ ] Season aggregation per player / team
- [ ] Nested endpoints: /teams/{id}/players, /matches/{id}/stats
- [ ] Advanced metrics (xG, pass completion, defensive ratings)

## Phase 4 — Mobile App
- [ ] Expo React Native project setup
- [ ] Authentication (JWT)
- [ ] Player and team detail screens
- [ ] Live match view (if data source supports it)

## Phase 5 — Production
- [ ] Deployment on Railway / Render / AWS
- [ ] CI/CD pipeline via GitHub Actions
- [ ] Monitoring and alerting
