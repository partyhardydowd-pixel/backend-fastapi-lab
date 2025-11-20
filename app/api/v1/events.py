from datetime import datetime

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.schemas.event import Event
from app.services.device_service import get_device, set_muted
from app.services.event_service import record_event
from app.services.rule_service import get_rules_for_trigger

router = APIRouter(prefix="/events", tags=["events"])


class CommercialEventIn(BaseModel):
    device_id: int
    timestamp: datetime | None = None


@router.post("/commercial-start", response_model=Event, status_code=status.HTTP_201_CREATED)
def commercial_start(payload: CommercialEventIn):
    device = get_device(payload.device_id)
    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found",
        )

    rules = get_rules_for_trigger("commercial_start")
    if rules:
        set_muted(device.id, True)

    event = record_event(
        device_id=device.id,
        event_type="commercial_start",
        timestamp=payload.timestamp,
    )
    return event


@router.post("/commercial-end", response_model=Event, status_code=status.HTTP_201_CREATED)
def commercial_end(payload: CommercialEventIn):
    device = get_device(payload.device_id)
    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Device not found",
        )

    rules = get_rules_for_trigger("commercial_start")
    if rules:
        set_muted(device.id, False)

    event = record_event(
        device_id=device.id,
        event_type="commercial_end",
        timestamp=payload.timestamp,
    )
    return event
