from typing import List

from app.schemas.rule import MuteRule


_rules: list[MuteRule] = []
_next_id: int = 1


def list_rules() -> List[MuteRule]:
    return list(_rules)


def create_rule(name: str, trigger: str, enabled: bool = True) -> MuteRule:
    global _next_id
    rule = MuteRule(
        id=_next_id,
        name=name,
        trigger=trigger,
        enabled=enabled,
    )
    _next_id += 1
    _rules.append(rule)
    return rule


def get_rules_for_trigger(trigger: str) -> List[MuteRule]:
    return [rule for rule in _rules if rule.trigger == trigger and rule.enabled]
