from sqlalchemy import select
from sqlalchemy.orm import Session

from models import OrderItem


def getItemsByOrderId(db: Session, order_id: int) -> list[OrderItem]:
    stmt = (
        select(OrderItem)
        .where(OrderItem.order_id == order_id)
        .order_by(OrderItem.product_id)
    )
    return list(db.scalars(stmt))
