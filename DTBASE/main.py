from fastapi import FastAPI
import models
from models import EmployeesModel , PassportModel
from database import engine, Base

Base.metadata.drop_all(bind=engine)    # ⚠️ Xóa sau khi chạy 1 lần!
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return { "message" : "Lấy dữ liệu thành công"}
