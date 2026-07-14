from fastapi import FastAPI , Depends
import models
from database import Base , engine , SessionLocal  , get_database
from models import EnrollmentModel , CourseModel , StudentModel , ProjectModel
from sqlalchemy.orm import Session , joinedload
from Schemals import StudentResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Đây là API trang LMS")

db = SessionLocal()

# nếu database chưa có gì thì đẩy dữ liệu mẫu vào database 
# if db.query(CourseModel).count() == 4 :
    # c1 = CourseModel(id = 2 , course_name = "Python" , money=2_000_000)
    # c2 = CourseModel(id = 3 , course_name = "ReactJS" , money=3_000_000)
    # c3 = CourseModel(id = 4 , course_name = "NestJS" , money=4_000_000)
    # db.add_all([c1,c2,c3])

    # st1 = StudentModel(name = "Đinh Văn Luyến" , email = "luyen@gmail.com")
    # db.add(st1)
    # db.commit()
    # er = EnrollmentModel(student_id=1 , course_id=1)
    # p1 = ProjectModel (project_name = "Pathway" , technology = "ReactJS , NestJs , NextJs" , day = "120" ,student_id = 1 )
    # db.add(p1)
    # db.commit()
@app.get("/")
def home():
    return {"message" : "Xin Chào FastAPI"}

@app.get("/students" , response_model=list[StudentResponse])
def get_all_student(db : Session = Depends(get_database)):
    return db.query(StudentModel).options(joinedload(StudentModel.projects)).all()