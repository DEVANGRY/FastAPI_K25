from fastapi import FastAPI, Depends
from database import Base ,engine , handle_get_db , SessionLocal
import models
from sqlalchemy.orm import Session 
from models import StudentModel , DepartmentModel , CourseModel , EnrollmentModel
from Schemal import StudentDetailInfo
Base.metadata.create_all(bind=engine)
app = FastAPI()
db = SessionLocal()

if db.query(DepartmentModel).count() == 0 :
    it_depart = DepartmentModel(id = 1 , name="IT")
    sell_depart = DepartmentModel(id = 2 ,name="Seller")
    db.add_all([it_depart , sell_depart])

    c1 = CourseModel(id=1, name="Python Fastapi", status="OPEN")
    c2 = CourseModel(id=2, name="Database Design", status="OPEN")
    c3 = CourseModel(id=3, name="Machine Learning", status="CLOSED")
    db.add_all([c1, c2, c3])

    # Thêm sinh viên
    s1 = StudentModel(id=1, full_name="Nguyen Van A", status="ACTIVE", department_id=1)
    s2 = StudentModel(id=2, full_name="Le Thi B", status="INACTIVE", department_id=2)
    db.add_all([s1, s2])

    db.flush()
    e1 = EnrollmentModel(id = 1 , student_id = 1 , course_id = 1)
    db.add(e1)
    db.commit()
db.close

@app.get("/students/{student_id}",response_model=StudentDetailInfo)
def handle_search_detail (student_id : int , db : Session = Depends(handle_get_db)):
    detail = db.query(StudentModel).filter(StudentModel.id == student_id).filter().first()
    return detail
