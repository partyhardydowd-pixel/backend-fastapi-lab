from fastapi import FastAPI

from app.api.v1.users import router as users_router
from app.api.v1.devices import router as devices_router
from app.api.v1.rules import router as rules_router
from app.api.v1.events import router as events_router

app = FastAPI(
    title="Backend Mastery API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(users_router, prefix="/api/v1")
app.include_router(devices_router, prefix="/api/v1")
app.include_router(rules_router, prefix="/api/v1")
app.include_router(events_router, prefix="/api/v1")
