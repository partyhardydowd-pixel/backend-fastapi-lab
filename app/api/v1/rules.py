from typing import List

from fastapi import APIRouter, status
from pydantic import BaseModel

from app.schemas.rule import MuteRule
from app.services.rule_service import list_rules, create_rule

router = APIRouter(prefix="/rules", tags=["rules"])


class RuleCreate(BaseModel):
    name: str
    trigger: str  # e.g. "commercial_start"
    enabled: bool = True


@router.get("", response_model=List[MuteRule])
def list_rules_endpoint():
    return list_rules()


@router.post("", response_model=MuteRule, status_code=status.HTTP_201_CREATED)
def create_rule_endpoint(payload: RuleCreate):
    return create_rule(
        name=payload.name,
        trigger=payload.trigger,
        enabled=payload.enabled,
    )
