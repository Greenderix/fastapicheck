from datetime import datetime
from typing import Any

from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base: Any = declarative_base()


class Skill(Base):
    __tablename__ = "skills"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String, nullable=False, unique=True)
    registered_at = Column("registered_at", TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column("hashed_password", String, nullable=False)
    is_superuser = Column("is_superuser", Boolean, default=False)
    skill_id = Column("skill_id", Integer, ForeignKey("skills.id"), nullable=True)
    level = Column("level", Integer, default=1)
    level_progress = Column("level_progress", Integer, default=0)
    arsenal = relationship("Arsenal", backref="user")


class Arsenal(Base):
    __tablename__ = "arsenals"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    # user = relationship("User", backref="arsenal")


association_table = Table(
    "arsenal_arsenal_item_con",
    Base.metadata,
    Column("arsenal_id", ForeignKey("arsenals.id")),
    Column("arsenal_item_id", ForeignKey("arsenal_items.id")),
)


class ArsenalItem(Base):
    __tablename__ = "arsenal_items"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    damage = Column("damage", Integer, nullable=False)
