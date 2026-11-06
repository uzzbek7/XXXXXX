from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Product


def get_by_id(db: Session, product_id: int) -> Product | None:
    return db.get(Product, product_id)


def get_all(db: Session) -> list[Product]:
    return list(db.scalars(select(Product).order_by(Product.id)))


def getProductByCategory(db: Session, category: str) -> list[Product]:
    stmt = select(Product).where(Product.category == category).order_by(Product.id)
    return list(db.scalars(stmt))
