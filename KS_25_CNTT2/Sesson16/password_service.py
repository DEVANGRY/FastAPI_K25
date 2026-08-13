import bcrypt 

def hash_password(raw_password : str) -> str : 
    password_bytes = raw_password.encode("utf-8")

    hasded = bcrypt.hashpw(password=password_bytes , salt=bcrypt.gensalt())

    return hasded.decode()


def verify_password (raw_password: str , stored_password : str) -> bool :
    return bcrypt.checkpw(
        raw_password.encode("utf-8"),
        stored_password.encode("utf-8")
    )

hash_01 = hash_password("Thanhliem123")

print(verify_password("Thanhliem123", hash_01))