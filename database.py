
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 🔹 PostgreSQL URL
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/nahum"

# 🔹 Engine (connect to DB)
engine = create_engine(DATABASE_URL)

# 🔹 Session (DB connection for each request)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 🔹 Base (for models)
Base = declarative_base()

# 🔹 Dependency for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()