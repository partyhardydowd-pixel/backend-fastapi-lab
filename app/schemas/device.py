from pydantic import BaseModel


class Device(BaseModel):
    id: int
    name: str
    type: str  # e.g. "tv", "receiver"
    is_muted: bool = False
