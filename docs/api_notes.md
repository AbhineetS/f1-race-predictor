# OpenF1 API Notes

This document summarizes the OpenF1 endpoints explored for the F1 Race Predictor project.
Source: https://openf1.org/docs

Note: the example responses below show the general structure and field names.
Actual values will vary each time the API is called, since they reflect real,
changing F1 data.

---

## Drivers

**Endpoint:** `https://api.openf1.org/v1/drivers`

**Purpose:** Get detailed information about the drivers participating in a session — name, team, car number.

**Important fields:**
- `driver_number` — the driver's car number for the season
- `full_name` — driver's full name
- `team_name` — the team they drive for
- `team_colour` — hex color code for the team (useful for UI styling)
- `headshot_url` — link to driver's photo

**Example response structure:**
```json
{
  "driver_number": 1,
  "full_name": "Max VERSTAPPEN",
  "team_name": "Red Bull Racing",
  "team_colour": "3671C6"
}
```

---

## Position

**Endpoint:** `https://api.openf1.org/v1/position`

**Purpose:** Get a driver's position throughout a session, including how it changes over time. This is not one record per driver — it's many records, one for each position change.

**Important fields:**
- `driver_number` — which driver this record is for
- `position` — their position at this point in time (1 = first place)
- `date` — timestamp of when this position was recorded
- `session_key` — which session this belongs to

**Example response structure:**
```json
{
  "driver_number": 40,
  "position": 2,
  "date": "2023-08-26T09:30:47.199000+00:00"
}
```

---

## Sessions

**Endpoint:** `https://api.openf1.org/v1/sessions`

**Purpose:** Get information about a session — a distinct period of track activity (Practice, Qualifying, Sprint, or Race) within a race weekend.

**Important fields:**
- `session_name` — e.g. "Race", "Qualifying", "Practice 1"
- `session_type` — broader category
- `circuit_short_name` — track name
- `country_name` — country where the event takes place
- `year` — season year
- `date_start` / `date_end` — when the session runs

**Example response structure:**
```json
{
  "session_name": "Race",
  "circuit_short_name": "Spa-Francorchamps",
  "country_name": "Belgium",
  "year": 2023
}
```

---

