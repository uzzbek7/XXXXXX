from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models import Order, OrderItem, Product


def get_by_id(db: Session, order_id: int) -> Order | None:
    return db.get(Order, order_id)


def get_all(db: Session) -> list[Order]:
    return list(db.scalars(select(Order).order_by(Order.id)))


def getOrdersBetweenDate(
    db: Session,
    start_date: datetime,
    end_date: datetime,
) -> list[Order]:
    stmt = (
        select(Order)
        .where(Order.created_at >= start_date, Order.created_at <= end_date)
        .order_by(Order.created_at, Order.id)
    )
    return list(db.scalars(stmt))


getOrdersBeetwinDate = getOrdersBetweenDate


def getByUserId(db: Session, user_id: int) -> list[Order]:
    stmt = select(Order).where(Order.user_id == user_id).order_by(Order.id)
    return list(db.scalars(stmt))


def add_order(db: Session, order: Order) -> Order:
    db.add(order)
    db.flush()
    return order


def getBestProductsRange(db: Session, limit: int = 10, offset: int = 0) -> list[Product]:
    sales = (
        select(OrderItem.product_id, func.sum(OrderItem.count).label("sales_count"))
        .group_by(OrderItem.product_id)
        .subquery()
    )
    stmt = (
        select(Product)
        .join(sales, Product.id == sales.c.product_id)
        .order_by(sales.c.sales_count.desc(), Product.id)
        .limit(limit)
        .offset(offset)
    )
    return list(db.scalars(stmt))
