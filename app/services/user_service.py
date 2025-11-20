from typing import List, Optional

from app.schemas.user import User


_FAKE_USERS: list[User] = [
    User(id=1, email="alice@example.com", is_active=True),
    User(id=2, email="bob@example.com", is_active=False),
]


def list_users() -> List[User]:
    return _FAKE_USERS


def get_user(user_id: int) -> Optional[User]:
    for user in _FAKE_USERS:
        if user.id == user_id:
            return user
    return None
