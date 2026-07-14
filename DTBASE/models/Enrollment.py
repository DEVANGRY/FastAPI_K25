from database import Base 
from sqlalchemy import Column , Integer , ForeignKey, Table

enrollment_table = Table(
    "enrollment_table" ,
    Base.metadata ,
    Column("employee_id" , Integer , ForeignKey("employee.id") , primary_key=True),
    Column("course_id" , Integer , ForeignKey("course.id") , primary_key=True),
)