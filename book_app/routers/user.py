
from fastapi import APIRouter,Depends

from book_app.services import user as crud

from book_app.db.database import get_db

from book_app.db.models.user import User
from book_app.schemas import user



from sqlalchemy.orm import Session

router=APIRouter(prefix="/user")




    


@router.get("/list")
def get_all_users(db: Session=Depends(get_db)):
    return crud.get_all_users(db)

    
@router.get("/{id}")
def get_user_by_id(id:int,db: Session=Depends(get_db)):
    return crud.get_user_by_id(id,db)

@router.post("")
def add_user(b:user.User,db: Session=Depends(get_db)):
    details=User(name=b.name,user_name=b.user_name,password=b.password,mail=b.mail)
    return crud.add_user(details,db)


@router.put("/{id}")
def update_user_by_id(id:int,updated_details:user.UpdateUser,db: Session=Depends(get_db)):
    return crud.update_user_by_id(id,updated_details,db)


@router.delete("/{id}")
def delete(id:int,db:Session=Depends(get_db)):
    return crud.delete_user(id,db)