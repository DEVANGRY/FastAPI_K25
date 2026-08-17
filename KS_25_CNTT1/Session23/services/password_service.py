import bcrypt
from datetime import datetime , timedelta , timezone
import jwt 

SECRET_KEY = "ajksfjkashfjkashjckaxbcjkasbjkfcbashbjasfkasjfkasnjknasjkvbasj" 
ALG = "HS256"

# Tạo hàm dùng để băm chuỗi mật khẩu
def handle_hash_password (password:str) -> str :
    return bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()

# Hàm này dùng để kiểm tra mật khẩu từ người dùng nhập lên với mật khẩu từ database
def handle_check_password (password : str , hash_password) -> bool :
    return bcrypt.checkpw(password.encode(),hash_password.encode())

# Hàm để tạo access_token 
def handle_create_access_token (user_id: int , username : str , role_user : str):
    time = datetime.now(timezone.utc)

    payload = {
        "sup" : user_id,
        "iat" : time,
        "exp" : time + timedelta(minutes=15),
        "username" : username,
        "role_user" : role_user
    }

    return jwt.encode(payload,SECRET_KEY,ALG)