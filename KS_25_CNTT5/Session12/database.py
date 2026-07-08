from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

# Bước 1 : Tạo một URL kết nối đến Database 
SQLAlCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/db_game_lol"

# Bước 2 : Tạo một engine cấu hình kết nối toàn bộ SQLAlCHEMY
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# Bước 3 : Tạo cấu hình một phiên xử lý API 
SessionLocal = sessionmaker(autoflush=False ,autocommit=False, bind=engine)

# Bước 4 : Tạo một Base => để cấu hình các table trong database 
Base = declarative_base()

# Bước 5 : Tạo một hàm để kết nối Database 
def handle_connect_DB ():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()