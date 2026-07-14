from sqlalchemy import Table, Column , Integer , ForeignKey
from database import Base
# Cách 1 : tạo bảng trung gian cho mối quan hệ thể hiện nhiều nhiều 
# enrollment_table = Table(
#     "enrollment",
#     Base.metadata,
#     Column("student_id" , Integer , ForeignKey("student.id")),
#     Column("course_id" , Integer , ForeignKey("course.id")),
# )

# Cách 2 : Tạo bảng 
class EnrollmentModel (Base) :
    __tablename__ = "enrollment"

    id = Column(Integer,primary_key=True , index=True)
    student_id = Column(Integer , ForeignKey("student.id"))
    course_id = Column(Integer , ForeignKey("course.id"))

