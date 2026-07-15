from fastapi import FastAPI , Depends
import models
from database import Base , engine , SessionLocal  , get_database

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Đây là API trang LMS")

db = SessionLocal()

@app.get("/")
def home():
    return {"message" : "Xin Chào FastAPI"}
