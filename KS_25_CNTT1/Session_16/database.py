from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base

# Bước 1 : Tạo một URL 
SQLAlCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/crm_lms"

# Bước 2 : Tạo một engine : Cầu nối giữa thằng sqlalchemy và thằng database
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# Bước 3 : cấu hình một phiên làm việc của các API 
SessionLocal = sessionmaker(autoflush=False,autocommit=False,bind=engine)

# Bước 4 : Tạo một Base để cấu hình models : Các cái bảng trong database 
Base = declarative_base()

# Bước cuối cùng : Tạo một hàm để chạy kết nối vào database 
def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

