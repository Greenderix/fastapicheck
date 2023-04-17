from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

lobby = Table(
    "lobby",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
)
