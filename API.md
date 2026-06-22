# API Documentation

## Overview
The F1 Live Leaderboard uses OpenF1 APIs to provide live Formula 1 race information.

## Endpoints

### GET /
Returns API status.

### GET /positions
Returns the latest race positions.

## Response Format

{
  "position": 1,
  "driver_number": 44,
  "name": "Lewis Hamilton",
  "team": "Ferrari"
}

## Future Endpoints

- /weather
- /session
- /drivers
- /telemetry
