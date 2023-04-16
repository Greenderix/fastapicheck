from sqlalchemy import MetaData, Table, Column, Integer

metadata = MetaData()

level = Table(
    "level",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("level_grade", Integer, nullable=False),
)
