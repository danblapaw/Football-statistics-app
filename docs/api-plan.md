# API Plan

Base URL: `/api`

**MVP scope: season 2025-2026 only.** All list endpoints default to `?season=2025-2026`.

All list endpoints support pagination via `?skip=0&limit=25`.

---

## Response Formats

### List response
```json
{
  "data": [...],
  "total": 100,
  "skip": 0,
  "limit": 25
}
```

### Detail response
Returns the resource object directly.

### Error response
```json
{ "detail": "Resource not found" }
```

---

## Endpoints

### Health
| Method | Path    | Status  | Description          |
|--------|---------|---------|----------------------|
| GET    | /health | ✅ Done | Service health check |

---

### Leagues — `/api/leagues`
| Method | Path              | Status     | Query params                        |
|--------|-------------------|------------|-------------------------------------|
| GET    | /api/leagues      | ✅ Done    | `skip`, `limit`, `season`           |
| GET    | /api/leagues/{id} | ✅ Done    |                                     |
| GET    | /api/leagues/{id}/teams   | 🔜 Planned |                           |
| GET    | /api/leagues/{id}/matches | 🔜 Planned |                           |

---

### Teams — `/api/teams`
| Method | Path            | Status     | Query params                          |
|--------|-----------------|------------|---------------------------------------|
| GET    | /api/teams      | ✅ Done    | `skip`, `limit`, `league_id`, `season`|
| GET    | /api/teams/{id} | ✅ Done    |                                       |
| GET    | /api/teams/{id}/players | 🔜 Planned |                               |
| GET    | /api/teams/{id}/stats   | 🔜 Planned |                               |

---

### Players — `/api/players`
| Method | Path              | Status     | Query params                         |
|--------|-------------------|------------|--------------------------------------|
| GET    | /api/players      | ✅ Done    | `skip`, `limit`, `team_id`, `season` |
| GET    | /api/players/{id} | ✅ Done    |                                      |
| GET    | /api/players/{id}/stats | 🔜 Planned |                              |

---

### Matches — `/api/matches`
| Method | Path              | Status     | Query params                                      |
|--------|-------------------|------------|---------------------------------------------------|
| GET    | /api/matches      | ✅ Done    | `skip`, `limit`, `league_id`, `season`, `status`  |
| GET    | /api/matches/{id} | ✅ Done    |                                                   |
| GET    | /api/matches/{id}/stats | 🔜 Planned |                                           |

---

## Season filter

The `season` query param is available on all list endpoints. Default value: `2025-2026`.

Pass `season=` (empty) to query across all seasons.

---

## Match status filter values
`scheduled` · `live` · `finished` · `postponed` · `cancelled`

---

## Planned (Phase 3)
- POST endpoints for data ingestion
- Aggregated season stats per player and team
- xG, pass completion, defensive rating endpoints
