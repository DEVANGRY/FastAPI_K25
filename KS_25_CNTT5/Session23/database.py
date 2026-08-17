from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

SQL_AlCHEMY_URL  = "mysql+pymysql://root:123456@localhost:3306/crm_banking"

engine = create_engine(SQL_AlCHEMY_URL)

SessionLocal = sessionmaker(autoflush=False , autocommit= False , bind=engine)

Base = declarative_base()

def get_db ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()