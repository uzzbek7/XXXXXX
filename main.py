from sqlalchemy import create_engine

from models import Base


def create_tables(database_url: str = "sqlite:///shop.db") -> None:
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()
