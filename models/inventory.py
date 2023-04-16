from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey

from models.item import item

metadata = MetaData()

inventory = Table(
    "inventory",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("item_id", Integer, ForeignKey(item.c.id)),
)
