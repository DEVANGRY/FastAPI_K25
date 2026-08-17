from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

URL = "mysql+pymysql://root:123456@localhost:3306/crm_lms_v2"

engine = create_engine(URL)

LocalSession = sessionmaker(autoflush=False,autocommit= False,bind=engine)

Base = declarative_base()

def connect_db ():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()