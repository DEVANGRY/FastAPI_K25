# Tạo các hàm để xử lý logic trực tiếp với DATABASE
from schemas import CreateAccountRequest , UpdateAccountV2Request
from sqlalchemy.orm import Session
from models import AccountUserModel

def create_account_service (new_account : CreateAccountRequest, db : Session):
    new_account_db = AccountUserModel(
        account= new_account.account,
        password= new_account.password,
        email= new_account.email,
        is_active= new_account.is_active,
    )

    db.add(new_account_db)

    db.commit()

    db.refresh(new_account_db)

    return new_account_db

def handle_get_all_account (db : Session): 
    list_account_db = db.query(AccountUserModel).all()
    return list_account_db


def update_account_service (account_id : int , update_account : CreateAccountRequest, db : Session):
    find_account_db = db.query(AccountUserModel).filter(AccountUserModel.id == account_id).first()

    if find_account_db :
        find_account_db.account = update_account.account
        find_account_db.password = update_account.password
        find_account_db.email = update_account.email
        find_account_db.is_active = update_account.is_active
        db.commit()
        db.refresh(find_account_db)

    return find_account_db


def delete_account_service (account_id : int , db : Session):
    find_account_db = db.query(AccountUserModel).filter(AccountUserModel.id == account_id).first()

    if find_account_db :
        db.delete(find_account_db)
        db.commit()
        return True
    return False

def handle_update_account_v2_service(account_id : int , account_update :UpdateAccountV2Request , db : Session):
    # Tìm kiếm có đối tượng trong DATABASE
    find_account_db = db.query(AccountUserModel).filter(AccountUserModel.id == account_id).first()
    if find_account_db:
        # ép kiểu find_account_db về dict 
        account_update_dict = account_update.model_dump(exclude_unset=True)
        for key,value in account_update_dict.items():
            setattr(find_account_db,key,value)
        db.commit()
        db.refresh(find_account_db)

    return find_account_db

# Sắp xếp
def handle_sort_by_id(db:Session) :

    list_account = db.query(AccountUserModel).order_by(AccountUserModel.id.desc()).all()