from schemas import CreateAccountRequest , UpdateAccountRequest
from sqlalchemy.orm import Session
from models import AccountUserModel

def handle_create_account_service(new_account : CreateAccountRequest , db : Session) : 
    new_account_db = AccountUserModel(
        username = new_account.username,
        password = new_account.password,
        email = new_account.email
    )

    db.add(new_account_db)

    db.commit()

    db.refresh(new_account_db)

    return new_account_db

def handle_get_all_account_service (db : Session):
    list_account_db = db.query(AccountUserModel).all()
    return list_account_db


def handle_update_account_service(account_id:int , data_update_account : UpdateAccountRequest , db : Session):
    find_account_user_db = db.query(AccountUserModel).filter(AccountUserModel.id == account_id).first()

    if find_account_user_db:
        find_account_user_db.username = data_update_account.username
        find_account_user_db.password = data_update_account.password
        find_account_user_db.email = data_update_account.email
        find_account_user_db.is_status = data_update_account.is_status

        db.commit()
        db.refresh(find_account_user_db)

    return find_account_user_db


def handle_delete_account_service(account_id:int , db : Session):
    find_account_user_db = db.query(AccountUserModel).filter(AccountUserModel.id == account_id).first()

    if find_account_user_db:
        db.delete(find_account_user_db)
        db.commit()
        return True

    return False