"""Create DB tables for dev (uses src.db.models.Base.metadata.create_all)."""
from src.db.db import engine
from src.db.models import Base
print("Creating tables...")
Base.metadata.create_all(engine)
print("Done.")
