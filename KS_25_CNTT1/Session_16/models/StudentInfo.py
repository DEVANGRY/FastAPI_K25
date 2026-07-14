from database import Base
from sqlalchemy import Column , Integer , String , ForeignKey
from sqlalchemy.orm import relationship

# Tạo model thông tin chi tiết của sinh viên

class StudentInfoModel(Base):
    __tablename__ = "student_info"

    id = Column(Integer,primary_key=True , index=True)
    age  = Column(Integer , nullable=False )
    passport  = Column(String(15) , nullable=False , unique=True)
    phone = Column(String(11) , nullable=False , unique=True)
    student_id = Column(Integer , ForeignKey("student.id") , unique=True )

    student = relationship("StudentModel",back_populates="student_info")

