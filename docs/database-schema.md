# Database Schema (Draft)

## Tables

### leagues
| Column      | Type    | Notes              |
|-------------|---------|---------------------|
| id          | UUID PK |                     |
| name        | TEXT    | e.g. "La Liga"      |
| country     | TEXT    |                     |
| season      | TEXT    | e.g. "2024-25"      |
| created_at  | TIMESTAMP |                   |

### teams
| Column      | Type    | Notes              |
|-------------|---------|---------------------|
| id          | UUID PK |                     |
| name        | TEXT    |                     |
| league_id   | UUID FK | → leagues.id        |
| founded     | INT     |                     |
| stadium     | TEXT    |                     |

### players
| Column      | Type    | Notes              |
|-------------|---------|---------------------|
| id          | UUID PK |                     |
| name        | TEXT    |                     |
| team_id     | UUID FK | → teams.id          |
| position    | TEXT    |                     |
| nationality | TEXT    |                     |
| birth_date  | DATE    |                     |

### matches
| Column       | Type      | Notes             |
|--------------|-----------|-------------------|
| id           | UUID PK   |                   |
| league_id    | UUID FK   | → leagues.id      |
| home_team_id | UUID FK   | → teams.id        |
| away_team_id | UUID FK   | → teams.id        |
| played_at    | TIMESTAMP |                   |
| home_score   | INT       |                   |
| away_score   | INT       |                   |

### player_stats
| Column       | Type    | Notes              |
|--------------|---------|--------------------|
| id           | UUID PK |                    |
| player_id    | UUID FK | → players.id       |
| match_id     | UUID FK | → matches.id       |
| goals        | INT     |                    |
| assists      | INT     |                    |
| minutes      | INT     |                    |
| yellow_cards | INT     |                    |
| red_cards    | INT     |                    |
| shots        | INT     |                    |
| passes       | INT     |                    |
| pass_accuracy| FLOAT   |                    |
