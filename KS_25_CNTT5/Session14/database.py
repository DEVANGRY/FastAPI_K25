from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
URL = "mysql+pymysql://root:123456@localhost:3306/library_db"

engine = create_engine(URL)

SessionLocal = sessionmaker(autoflush=False,autocommit=False , bind=engine)

Base = declarative_base()

def handle_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

    