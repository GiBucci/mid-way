from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

app = FastAPI(
    title="mid-way",
    description="Find fair and comfortable meeting places for groups.",
    version="0.1.0",
)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
