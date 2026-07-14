from database import Base 
from sqlalchemy import Column , Integer , String  , Table , ForeignKey
from sqlalchemy.orm import relationship

class EnrollmentModel(Base) :
    __tablename__ = "enrollment"
    id = Column(Integer,primary_key=True,autoincrement=True,index=True)
    student_id = Column(Integer , ForeignKey("student.id"),nullable=False)
    course_id = Column(Integer , ForeignKey("course.id"),nullable=False)
