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

## Setup Guide

This guide assumes you have never worked on this repository before.

### 1. Install the Required Tools

Install these tools first:

- **Git:** used to download the repository and send changes back to GitHub.
- **Python 3.13:** the programming language used by the project.
- **uv:** used to create the local Python environment and install dependencies.

On Windows, after installing `uv`, you may need to close and reopen PowerShell before the `uv`
command is available.

Check that the tools are installed:

```powershell
git --version
python --version
uv --version
```

### 2. Download the Repository

Choose a folder where you keep projects, then run:

```powershell
git clone https://github.com/GiBucci/mid-way.git
cd mid-way
```

### 3. Create the Python Environment

Run this once after cloning the repository:

```powershell
uv sync
```

This creates a local `.venv` folder and installs the dependencies listed in
`pyproject.toml` and `uv.lock`.

### 4. Check That Everything Works

Run the code quality check:

```powershell
uv run ruff check .
```

Run the formatter:

```powershell
uv run ruff format .
```

Run the tests:

```powershell
uv run pytest
```

At this stage, the project may not have tests yet. If pytest says `no tests ran`, that is fine
until application code is added.

## Working on Changes

Do not work directly on `main`. Create a branch for every change.

### Branch Names

Use clear branch prefixes:

- `feature/...` for new features.
- `fix/...` for bug fixes.
- `docs/...` for documentation-only changes.
- `chore/...` for project setup, dependency, or maintenance changes.
- `refactor/...` for code structure changes that do not change behavior.
- `test/...` for adding or improving tests.

Examples:

```powershell
git switch -c feature/event-creation
git switch -c fix/location-validation
git switch -c docs/setup-guide
git switch -c chore/update-ruff-config
```

### Daily Workflow

Before starting work, update your local `main` branch:

```powershell
git switch main
git pull
```

Create your branch:

```powershell
git switch -c feature/short-description
```

Make your changes, then check what changed:

```powershell
git status
git diff
```

Run the project checks before committing:

```powershell
uv run ruff format .
uv run ruff check .
uv run pytest
```

Commit your work:

```powershell
git add .
git commit -m "Short description of the change"
```

Push your branch to GitHub:

```powershell
git push -u origin feature/short-description
```

Then open a pull request on GitHub and ask for review.

### Commit Message Guidelines

Use short, specific commit messages. A good commit message says what changed, not just that
something was updated.

Good examples:

- `Add event creation draft`
- `Fix participant travel mode validation`
- `Document local setup workflow`

Avoid vague messages:

- `Update`
- `Fix stuff`
- `Changes`

### Pull Request Checklist

Before opening a pull request, make sure:

- The branch name follows the project convention.
- `uv run ruff format .` has been run.
- `uv run ruff check .` passes.
- `uv run pytest` passes, or there is a clear reason why tests are not available yet.
- The pull request description explains what changed and why.

No application code has been added yet. This repository currently contains only the first
product/technology draft and project tooling configuration.
