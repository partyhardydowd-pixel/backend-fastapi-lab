from datetime import datetime
from typing import List

from app.schemas.event import Event


_events: list[Event] = []
_next_id: int = 1


def list_events() -> List[Event]:
    return list(_events)


def record_event(device_id: int, event_type: str, timestamp: datetime | None = None) -> Event:
    global _next_id
    if timestamp is None:
        timestamp = datetime.utcnow()
    event = Event(
        id=_next_id,
        device_id=device_id,
        event_type=event_type,
        timestamp=timestamp,
    )
    _next_id += 1
    _events.append(event)
    return event
