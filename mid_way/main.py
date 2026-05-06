from fastapi import FastAPI

app = FastAPI(
    title="mid-way",
    description="Find fair and comfortable meeting places for groups.",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
