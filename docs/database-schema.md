# Database Schema

All tables use `String(36)` UUIDs as primary keys generated at application level.
Timestamps (`created_at`, `updated_at`) are managed via `TimestampMixin` using `server_default=func.now()`.

---

## Enums

### `position_enum`
| Value        |
|--------------|
| `goalkeeper` |
| `defender`   |
| `midfielder` |
| `forward`    |

### `match_status_enum`
| Value        |
|--------------|
| `scheduled`  |
| `live`       |
| `finished`   |
| `postponed`  |
| `cancelled`  |

---

## Tables

### `leagues`
| Column      | Type         | Constraints        | Notes                   |
|-------------|--------------|--------------------|-------------------------|
| id          | String(36)   | PK                 | UUID                    |
| name        | String(100)  | NOT NULL           | e.g. "La Liga"          |
| country     | String(100)  | NOT NULL           |                         |
| season      | String(20)   | NOT NULL           | e.g. "2024-25"          |
| logo_url    | String(500)  | nullable           |                         |
| created_at  | DateTime(tz) | NOT NULL           | server default: now()   |
| updated_at  | DateTime(tz) | NOT NULL           | auto-updated on change  |

---

### `teams`
| Column      | Type         | Constraints              | Notes                  |
|-------------|--------------|--------------------------|------------------------|
| id          | String(36)   | PK                       | UUID                   |
| league_id   | String(36)   | FK → leagues.id RESTRICT | NOT NULL               |
| name        | String(100)  | NOT NULL                 |                        |
| short_name  | String(10)   | nullable                 | e.g. "BAR"             |
| founded     | Integer      | nullable                 |                        |
| stadium     | String(150)  | nullable                 |                        |
| logo_url    | String(500)  | nullable                 |                        |
| created_at  | DateTime(tz) | NOT NULL                 |                        |
| updated_at  | DateTime(tz) | NOT NULL                 |                        |

---

### `players`
| Column        | Type              | Constraints              | Notes                  |
|---------------|-------------------|--------------------------|------------------------|
| id            | String(36)        | PK                       | UUID                   |
| team_id       | String(36)        | FK → teams.id RESTRICT   | NOT NULL               |
| name          | String(150)       | NOT NULL                 |                        |
| nationality   | String(100)       | nullable                 |                        |
| position      | position_enum     | nullable                 |                        |
| birth_date    | Date              | nullable                 |                        |
| jersey_number | Integer           | nullable                 |                        |
| photo_url     | String(500)       | nullable                 |                        |
| created_at    | DateTime(tz)      | NOT NULL                 |                        |
| updated_at    | DateTime(tz)      | NOT NULL                 |                        |

---

### `matches`
| Column        | Type                | Constraints               | Notes                      |
|---------------|---------------------|---------------------------|----------------------------|
| id            | String(36)          | PK                        | UUID                       |
| league_id     | String(36)          | FK → leagues.id RESTRICT  | NOT NULL                   |
| home_team_id  | String(36)          | FK → teams.id RESTRICT    | NOT NULL                   |
| away_team_id  | String(36)          | FK → teams.id RESTRICT    | NOT NULL                   |
| played_at     | DateTime(tz)        | nullable                  |                            |
| status        | match_status_enum   | NOT NULL                  | default: `scheduled`       |
| home_score    | Integer             | nullable                  | null until match ends      |
| away_score    | Integer             | nullable                  |                            |
| matchday      | Integer             | nullable                  | round number in season     |
| created_at    | DateTime(tz)        | NOT NULL                  |                            |
| updated_at    | DateTime(tz)        | NOT NULL                  |                            |

---

### `player_stats`
| Column           | Type         | Constraints               | Notes                      |
|------------------|--------------|---------------------------|----------------------------|
| id               | String(36)   | PK                        | UUID                       |
| player_id        | String(36)   | FK → players.id CASCADE   | NOT NULL                   |
| match_id         | String(36)   | FK → matches.id CASCADE   | NOT NULL                   |
| minutes_played   | Integer      | nullable                  |                            |
| started          | Boolean      | NOT NULL                  | default: false             |
| goals            | Integer      | NOT NULL                  | default: 0                 |
| assists          | Integer      | NOT NULL                  | default: 0                 |
| shots            | Integer      | NOT NULL                  | default: 0                 |
| shots_on_target  | Integer      | NOT NULL                  | default: 0                 |
| passes           | Integer      | NOT NULL                  | default: 0                 |
| passes_completed | Integer      | NOT NULL                  | default: 0                 |
| key_passes       | Integer      | NOT NULL                  | default: 0                 |
| tackles          | Integer      | NOT NULL                  | default: 0                 |
| interceptions    | Integer      | NOT NULL                  | default: 0                 |
| clearances       | Integer      | NOT NULL                  | default: 0                 |
| yellow_cards     | Integer      | NOT NULL                  | default: 0                 |
| red_cards        | Integer      | NOT NULL                  | default: 0                 |
| xg               | Float        | nullable                  | expected goals             |
| xg_assist        | Float        | nullable                  | expected assisted goals    |
| rating           | Float        | nullable                  | match rating (0–10)        |
| created_at       | DateTime(tz) | NOT NULL                  |                            |
| updated_at       | DateTime(tz) | NOT NULL                  |                            |

---

## Relationship Map

```
League ──< Team ──< Player ──< PlayerStats
  └──────────────< Match >────────────────┘
                  (home_team_id, away_team_id → Team)
```

- `League` → `Team`: one-to-many
- `League` → `Match`: one-to-many
- `Team` → `Player`: one-to-many
- `Team` → `Match`: one-to-many (as home) + one-to-many (as away)
- `Player` → `PlayerStats`: one-to-many
- `Match` → `PlayerStats`: one-to-many
