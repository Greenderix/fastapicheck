import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from models.user import user

metadata = MetaData()

login_history = Table(
    "login_history",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("login_at", TIMESTAMP, default=datetime.utcnow),
    Column("login_id", Integer, ForeignKey(user.c.id))
)
