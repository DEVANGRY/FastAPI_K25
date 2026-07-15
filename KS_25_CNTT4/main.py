from fastapi import FastAPI 
from database import Base , engine
import models
from routers.Project import router as ProjectRouter
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(ProjectRouter)

@app.get("/")
def home():
    return {"message" : "Dữ liệu thành công"}
