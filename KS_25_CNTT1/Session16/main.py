from fastapi import FastAPI 
from database import Base , engine
import models
from routers.project_router import router as project_router 

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(project_router)

@app.get("/")
def home():
    return {"message" : "Dữ liệu thành công"}
