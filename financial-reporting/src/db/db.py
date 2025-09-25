"""DB engine and session helper."""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Default to sqlite for quick local dev; replace with POSTGRES URL via env var in production
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///data/dev.db")

engine = create_engine(DATABASE_URL, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
