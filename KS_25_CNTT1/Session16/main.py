from fastapi import FastAPI ,Request
from database import Base , engine
import models
from routers.project_router import router as project_router 
from fastapi.middleware.cors import CORSMiddleware
import time 

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.middleware("http")
async def log_request_middleware (request : Request , call_next):
    start_time = time.time()

    # CHo phép các request đi tiếp vào các API bên trong 
    response = await call_next(request)

    process_time = time.time() - start_time
    print(f"Log: Đoạn đường {request.url.path} mất {process_time:.4f} giây để hoàn thành")
    return response


app.include_router(project_router)

@app.get("/")
def home():
    return {"message" : "Dữ liệu thành công"}
