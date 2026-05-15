# API Plan

Base URL: `/api`

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
| Method | Path      | Status | Description          |
|--------|-----------|--------|----------------------|
| GET    | /health   | ✅ Done | Service health check |

---

### Leagues — `/api/leagues`
| Method | Path                  | Status | Query params         | Description          |
|--------|-----------------------|--------|----------------------|----------------------|
| GET    | /api/leagues          | ✅ Done | `skip`, `limit`      | List all leagues     |
| GET    | /api/leagues/{id}     | ✅ Done |                      | Get league by ID     |
| GET    | /api/leagues/{id}/teams   | 🔜 Planned |              | Teams in a league    |
| GET    | /api/leagues/{id}/matches | 🔜 Planned |              | Matches in a league  |

---

### Teams — `/api/teams`
| Method | Path                  | Status | Query params                   | Description          |
|--------|-----------------------|--------|--------------------------------|----------------------|
| GET    | /api/teams            | ✅ Done | `skip`, `limit`, `league_id`   | List teams           |
| GET    | /api/teams/{id}       | ✅ Done |                                | Get team by ID       |
| GET    | /api/teams/{id}/players   | 🔜 Planned |                        | Squad list           |
| GET    | /api/teams/{id}/stats     | 🔜 Planned |                        | Team season stats    |

---

### Players — `/api/players`
| Method | Path                  | Status | Query params                  | Description          |
|--------|-----------------------|--------|-------------------------------|----------------------|
| GET    | /api/players          | ✅ Done | `skip`, `limit`, `team_id`    | List players         |
| GET    | /api/players/{id}     | ✅ Done |                               | Get player by ID     |
| GET    | /api/players/{id}/stats   | 🔜 Planned |                       | Career / season stats|

---

### Matches — `/api/matches`
| Method | Path                  | Status | Query params                             | Description          |
|--------|-----------------------|--------|------------------------------------------|----------------------|
| GET    | /api/matches          | ✅ Done | `skip`, `limit`, `league_id`, `status`   | List matches         |
| GET    | /api/matches/{id}     | ✅ Done |                                          | Get match by ID      |
| GET    | /api/matches/{id}/stats   | 🔜 Planned |                                  | Per-player stats     |

---

## Match status filter values
`scheduled` · `live` · `finished` · `postponed` · `cancelled`

---

## Planned (Phase 3)
- POST endpoints for data ingestion
- Aggregated season stats per player and team
- xG, pass completion, defensive rating endpoints
