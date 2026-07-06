from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Bước 1 : Tạo một biến global để chứa đường dẫn kết nối 
# đến database của dự án 

# Cú pháp: mysql+pymysql://<username>:<password>@<host>:<port>/<db_name>
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/db_quan_ly_cua_hang"

# Bước 2 : Tạo engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Bước 3 : Tạo Session : phiên đăng nhập 
SessionLocal = sessionmaker(autoflush=False , autocommit=False , bind=engine)

# Bước 4 : Khởi tạo Base để tạo ra những Schema
Base = declarative_base()

# Hàm dùng để chạy kết nối vào database
def get_db () :
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()