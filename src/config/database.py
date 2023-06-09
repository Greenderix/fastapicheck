from functools import lru_cache
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.config.settings import get_settings

engine = create_engine(get_settings().DATABASE_URL, pool_pre_ping=True)


@lru_cache
def create_session() -> scoped_session:
    session: scoped_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


def get_session() -> Generator[scoped_session, None, None]:
    session: scoped_session = create_session()
    try:
        yield session
    finally:
        session.remove()
