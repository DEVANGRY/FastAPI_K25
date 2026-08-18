from pydantic import BaseModel

# API : register (Đăng ký)

# Đầu vào : request (username , password , email)

class RegisterRequest (BaseModel):
    username : str 
    password : str 
    email : str


class RegisterReponse (BaseModel):
    message : str

class LoginRequest (BaseModel):
    username : str 
    password : str

class LoginResponse (BaseModel):
    message: str 
    access_token : str 
    type_token : str