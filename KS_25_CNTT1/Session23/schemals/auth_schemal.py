from pydantic import BaseModel

class FormLoginRequest (BaseModel):
    username : str
    password : str


class LoginResponse (BaseModel):
    access_token : str 
    type_token : str