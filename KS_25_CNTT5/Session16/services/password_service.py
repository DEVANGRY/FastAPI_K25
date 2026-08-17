import bcrypt

# Xây dựng hàm để băm mật khẩu (hash password)

def hash_password(password : str) -> str :
    convert_password_bytes = password.encode() 
    hashed = bcrypt.hashpw(convert_password_bytes,bcrypt.gensalt(12))

    return hashed.decode()

# Xây dựng hàm để kiểm tra mật khẩu từ người dùng nhập với mật khẩu khi đã băm 
def check_password (password : str , hash_password : str) -> bool :
    return bcrypt.checkpw(password.encode() , hash_password.encode())


hash_01 = hash_password("12341asas")
password = "12341asas"

print(check_password(password,hash_01))