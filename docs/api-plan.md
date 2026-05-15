# API Plan

Base URL: `/api/v1`

## Endpoints

### Health
| Method | Path      | Description        |
|--------|-----------|--------------------|
| GET    | /health   | Service health check |

### Leagues
| Method | Path                  | Description          |
|--------|-----------------------|----------------------|
| GET    | /leagues              | List all leagues     |
| GET    | /leagues/{id}         | Get league details   |
| GET    | /leagues/{id}/teams   | Teams in a league    |
| GET    | /leagues/{id}/matches | Matches in a league  |

### Teams
| Method | Path                  | Description          |
|--------|-----------------------|----------------------|
| GET    | /teams                | List teams           |
| GET    | /teams/{id}           | Team detail          |
| GET    | /teams/{id}/players   | Squad list           |
| GET    | /teams/{id}/stats     | Team season stats    |

### Players
| Method | Path                  | Description          |
|--------|-----------------------|----------------------|
| GET    | /players              | List players         |
| GET    | /players/{id}         | Player detail        |
| GET    | /players/{id}/stats   | Career / season stats|

### Matches
| Method | Path                  | Description          |
|--------|-----------------------|----------------------|
| GET    | /matches              | List matches         |
| GET    | /matches/{id}         | Match detail         |
| GET    | /matches/{id}/stats   | Per-player stats     |

## Response Format
All responses follow:
```json
{
  "data": {},
  "meta": {
    "page": 1,
    "per_page": 25,
    "total": 100
  }
}
```
