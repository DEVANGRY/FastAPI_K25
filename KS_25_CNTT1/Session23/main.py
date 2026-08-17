from database import Base,engine
import models
from fastapi import FastAPI , Request
from routers.auth_router import auth_router
from fastapi.middleware.cors import CORSMiddleware
import time

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 3  API : 
# API 1 : Login 
# API 2 : register
# API 3 : Kiểm tra thông tin người dùng 
app.include_router(auth_router)

list_origins = [
    "http://localhost:3000/",
    "http://localhost:3001/",
    "http://localhost:8000/",
]

# CORS : Chặn các URL từ bên ngoài
app.add_middleware(
    CORSMiddleware,
    allow_origins=list_origins,
    allow_credentials=True,
    allow_methods=["*"]
)

# middleware : Để đo thời gian một API chạy từ lúc gọi đến lúc hoàn thành 
@app.middleware("http")
async def handle_calc_time_call_api (request : Request , call_next):
    start_time = time.time()

    response = await call_next(request)

    now_time = time.time() - start_time
    print(now_time)
    return  response


@app.get("/")
def hello_world():
    return {"message" :"Hello world"}