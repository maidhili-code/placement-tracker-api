from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine, inspect, text

DATABASE_URL = "sqlite:///./placement.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

class Base(DeclarativeBase):
    pass

SessionLocal = sessionmaker(bind=engine, autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        from sqlalchemy import inspect, text

columns = [
    col["name"]
    for col in inspect(engine).get_columns("applications")
]

if "user_id" not in columns:
    with engine.begin() as conn:
        conn.execute(
            text(
                "ALTER TABLE applications "
                "ADD COLUMN user_id INTEGER REFERENCES users(id)"
            )
        )

print("Database migration completed!")