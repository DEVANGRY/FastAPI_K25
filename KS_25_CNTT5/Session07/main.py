from fastapi import FastAPI , status , Request
from pydantic import BaseModel 
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import HTTPException

app = FastAPI()
list_account = [
    {"username": "tuanlq","phone": "09999999","address": "tang","password" : "demo123"},
    {"username": "tuanlq","phone": None ,"address": "tang","password" : "demo123"}
]

class AccountCreate(BaseModel):
    username : str
    password : str
    phone : str
    address : str

class AccountResponse(BaseModel):
    username : str
    phone : str
    address : str


@app.get("/list_account", response_model_exclude_none=True)
def handle_create_todo():
    return list_account

# Tạo một API để tạo tài khoản mới 
@app.post("/register" , response_model = AccountResponse ,status_code= status.HTTP_201_CREATED)
def handle_create_todo(account_new : AccountCreate ):
    list_account.append(account_new.model_dump())
    return account_new

# Bộ quy chuẩn mà response phản hồi về cho phía client 
def create_response(
    status_code: int,
    message: str,
    success: bool = False,
    data=None,
    errors=None,
):
 return JSONResponse(
    status_code=status_code,
    content={
        "success": success,
        "statusCode": status_code,
        "message": message,
        "data": data,
        "errors": errors
    }
 )

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
   return create_response(
   status_code=422,
   message="Dữ liệu gửi lên không hợp lệ",
   errors=exc.errors(),
 )

# Chốt 2: Bắt lỗi logic  1: Bắt lỗi validation (sai định dạng, thiếu field)
@app.exception_handler(HTTPException)
def http_exception_handler(request: Request, exc: HTTPException):
   return create_response(
     status_code=exc.status_code,
     message=exc.detail,
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