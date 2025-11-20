from datetime import datetime

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    device_id: int
    event_type: str  # "commercial_start" or "commercial_end"
    timestamp: datetime
