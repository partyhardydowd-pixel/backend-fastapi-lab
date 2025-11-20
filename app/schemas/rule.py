from pydantic import BaseModel


class MuteRule(BaseModel):
    id: int
    name: str
    trigger: str  # e.g. "commercial_start"
    enabled: bool = True
