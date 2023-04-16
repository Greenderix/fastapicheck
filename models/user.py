from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, JSON, Boolean

from models.inventory import inventory
from models.level import level
from models.lobby import lobby
from models.skill import skill
from models.role import role

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("skill_id", Integer, ForeignKey(skill.c.id)),
    Column("role_id", Integer, ForeignKey(role.c.id)),
    Column("level_id", Integer, ForeignKey(level.c.id)),
    Column("lobby_id", Integer, ForeignKey(lobby.c.id)),
    Column("inventory_id", Integer, ForeignKey(inventory.c.id)),

)
