from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
URL = "mysql+pymysql://root:123456@localhost:3306/db_crm_shope"

engine = create_engine(URL)

SessionLocal = sessionmaker(autoflush=False , autocommit= True , bind=engine)

Base = declarative_base()

def handle_get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()