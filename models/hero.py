from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Boolean

from models.ability import ability
from models.characteristic import characteristic

metadata = MetaData()

hero = Table(
    "hero",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("ability_id", Integer, ForeignKey(ability.c.id)),
    Column("characteristic_id", Integer, ForeignKey(characteristic.c.id)),
)
