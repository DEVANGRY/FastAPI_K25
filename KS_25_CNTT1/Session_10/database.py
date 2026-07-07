from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Bước 1 : Tạo một URL để cấu hình kết nối với database
# mysql+pymysql://<username>:<password>@<host>:<port>/<db_name>
SQLAlCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/db_quan_ly_sinh_vien"

# Bước 2 : Tạo engine : Cầu nối để kết nối vào database
engine = create_engine(SQLAlCHEMY_DATABASE_URL)

# Bước 3 : Tạo cấu hình phiên xử lí 
SessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)

# Bước 4 : Tạo Base - Tạo cấu hình cho các models
Base = declarative_base()

# Bước cuối cùng :Tạo hàm để khởi chạy database

def get_db():
    # Mở phiên xử lý vào database
    db = SessionLocal()
    try: 
        yield db
    finally:
        # đóng phiên xử lý database đó 
        db.close()