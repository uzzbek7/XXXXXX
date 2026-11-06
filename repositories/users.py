from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User


def get_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)


def getByName(db: Session, user_name: str) -> list[User]:
    stmt = select(User).where(User.name == user_name).order_by(User.id)
    return list(db.scalars(stmt))
