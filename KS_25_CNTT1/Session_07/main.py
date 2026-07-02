from fastapi import FastAPI , status 
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

app = FastAPI()

class AccountCreate(BaseModel):
    user_name : str = Field(...,min_length=5,description="Đây là lưu tên tài khoản")
    password: str 
    phone : str | None = None
    role : str

class AccountResponse(BaseModel):
    user_name : str = Field(...,min_length=5,description="Đây là lưu tên tài khoản")
    phone : str | None = None
    role : str


list_account = [{"user_name":"123" , "password":"1234" , "role" : "admin"}]
@app.post("/register", response_model_exclude_unset=True , status_code=status.HTTP_201_CREATED)
def handle_register (account_new : AccountCreate) :
    list_account.append(account_new.model_dump())
    return account_new

from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

def create_response(
   status_code: int,
   message: str,
   success: bool = False,
   data=None,
   errors=None,
   path=""
):
 return JSONResponse(
   status_code=status_code,
     content={
     "success": success,
     "statusCode": status_code,
     "message": message,
     "data": data,
     "errors": errors,
     "timestamp": datetime.utcnow().isoformat() + "Z",
     "path": path
   }
 )

# Chốt 1: Bắt lỗi validation (sai định dạng, thiếu field)
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
   return create_response(
   status_code=422,
   message="Dữ liệu gửi lên không hợp lệ",
   errors=exc.errors(),
   path=request.url.path
 )

# Chốt 2: Bắt lỗi logic nghiệp vụ (raise HTTPException)
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
   return create_response(
     status_code=exc.status_code,
     message=exc.detail,
     path=request.url.path
 )

# Chốt 3: "Hố đen" nuốt mọi lỗi hệ thống chưa lường trước
@app.exception_handler(Exception)
def global_exception_handler(request: Request, exc: Exception):
   print(f"[INTERNAL ERROR] Path: {request.url.path} | {str(exc)}")
   return create_response(
   status_code=500,
   message="Hệ thống gặp sự cố. Vui lòng thử lại sau.",
   path=request.url.path
 )
