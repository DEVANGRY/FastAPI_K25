from fastapi import FastAPI
import models
from database import Base , engine , SessionLocal
from models import EnrollmentModel , CourseModel

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Đây là API trang LMS")

db = SessionLocal()

# nếu database chưa có gì thì đẩy dữ liệu mẫu vào database 
if db.query(CourseModel).count() == 0 :
    c1 = CourseModel(id = 1 , course_name = "FastAPI" , money=1_000_000)
    db.add(c1)
    db.commit()


@app.get("/")
def home():
    return {"message" : "Xin Chào FastAPI"}