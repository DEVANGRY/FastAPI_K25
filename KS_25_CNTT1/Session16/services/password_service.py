import bcrypt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Hàm dùng để chuyển chuỗi mật khẩu => hash (Băm)
def handle_convert_hash_password(raw_password : str) -> str:
# bytes
    bytes_password = raw_password.encode("utf-8")
    hasded = bcrypt.hashpw(bytes_password,salt=bcrypt.gensalt())

    return hasded.decode()

# Hàm để check mật khẩu 
def very_password (raw_password : str , hash_password : str) -> bool: 
    return bcrypt.checkpw(raw_password.encode("utf-8"),hash_password.encode("utf-8"))


hash_01 = handle_convert_hash_password("123456")

print(very_password("12345",hash_01))