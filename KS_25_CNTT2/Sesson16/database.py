from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
URL = "mysql+pymysql://root:123456@localhost:3306/db_manager_user"

engine = create_engine(URL)

SessionLocal = sessionmaker(autoflush=False , autocommit= False , bind=engine)

Base = declarative_base()

def handle_get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()