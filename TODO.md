# TODO

This file tracks the first features and setup tasks for mid-way. Keep items small enough that a
new contributor can pick one up in a focused branch.

## Project Foundation

- [x] Create the initial FastAPI app structure.
- [x] Add a health check endpoint.
- [ ] Add a basic Jinja page layout.
- [ ] Add HTMX and Tailwind CSS to the frontend scaffold.
- [ ] Add a simple local development command to the README once the app exists.

## Event Creation

- [ ] Define the event data model.
- [ ] Create a page where an organizer can create an event.
- [ ] Add fields for event name, date, city or area, and optional place category.
- [ ] Generate a shareable event link after creation.

## Participant Input

- [ ] Define supported travel modes.
- [ ] Create a participant form for name, starting location, and preferred travel mode.
- [ ] Validate required participant fields.
- [ ] Show the list of participants already added to an event.

## Meeting Place Suggestions

- [ ] Define the first scoring formula for candidate meeting places.
- [ ] Start with simple distance-based scoring before adding routing APIs.
- [ ] Explain why each suggested place was ranked highly.
- [ ] Add room for future travel-time estimates by mode.

## Maps and Locations

- [ ] Add Leaflet to display event area and candidate places.
- [ ] Decide the first geocoding provider for converting addresses to coordinates.
- [ ] Store latitude and longitude for participant locations.
- [ ] Add clear error messages for locations that cannot be found.

## Quality and Collaboration

- [x] Add the first pytest test once application code exists.
- [ ] Add CI checks for Ruff and pytest.
- [ ] Keep new work on branches named `feature/...`, `fix/...`, `docs/...`, `chore/...`,
      `refactor/...`, or `test/...`.
