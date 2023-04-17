from sqlalchemy import MetaData, Table, Column, Integer, String, Boolean

metadata = MetaData()

characteristic = Table(
    "characteristic",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("description", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
)
