# mid-way

mid-way helps groups choose a fair meeting place.

An organizer creates an event and shares an invite with friends. Each participant adds their starting location and preferred travel mode, such as walking, bike, public transport, car, or metro. The app compares realistic travel effort across the group and suggests meeting places that are comfortable for everyone instead of simply picking a geographic midpoint.

## Product Draft

### Core Flow

1. Create an event with a name, date, city or area, and optional place categories.
2. Share the event link with participants.
3. Participants enter their location and preferred travel mode.
4. mid-way estimates travel time and distance for each participant.
5. The app ranks candidate meeting places by group fairness, total travel effort, and practical constraints.
6. The organizer reviews the suggested places and confirms the final meeting point.

### Early Product Principles

- Comfort matters more than mathematical midpoint distance.
- Travel time should be weighted above straight-line distance.
- The result should explain why a place was suggested.
- Participants should not need an account for the first version.
- The interface should feel fast on mobile, since invite links will often be opened from chat apps.

## Technology Draft

The project should stay Python-first, with a pragmatic web UI.

### Recommended Stack

- **Runtime and package management:** Python 3.13 with `uv`.
- **Backend:** FastAPI for HTTP APIs, validation, and future async routing/geocoding calls.
- **UI:** Server-rendered FastAPI pages with Jinja templates, HTMX for lightweight interactivity, and Tailwind CSS for styling.
- **Maps:** Leaflet for interactive maps in the browser.
- **Data validation:** Pydantic.
- **Persistence:** SQLite for the prototype, with a path to PostgreSQL when accounts, teams, or production hosting are needed.
- **Code quality:** Ruff for linting and formatting.
- **Testing:** pytest once application behavior starts being implemented.

### Why This UI Choice

Jinja plus HTMX keeps most application logic in Python while still allowing a responsive, app-like web experience. It avoids committing early to a large JavaScript frontend, but leaves room to introduce one later if the product needs richer map editing, real-time collaboration, or complex client-side state.

## Tooling

Install `uv`, then run:

```powershell
uv sync
```

Useful commands:

```powershell
uv run ruff check .
uv run ruff format .
uv run pytest
```

No application code has been added yet. This repository currently contains only the first product/technology draft and project tooling configuration.
