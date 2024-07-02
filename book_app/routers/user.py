
from fastapi import APIRouter,Depends

from book_app.schemas.token import TokenData
from book_app.services import user as crud

from book_app.db.database import get_db

from book_app.db.models.user import User
from book_app.schemas import user

from fastapi_pagination import paginate,Page,Params


from sqlalchemy.orm import Session

from book_app.services.hassing import Hash 

from . import oauth2

router=APIRouter(prefix="/user",
                 tags=['User']
)



@router.get("/list",response_model=list[user.UserOut])
def get_all_users(db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    return crud.get_all_users(db)

    

@router.post("")
def add_user(b:user.User,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    
    hash=Hash()

    details=User(name=b.name,user_name=b.user_name,password=hash.bcrypt(b.password),mail=b.mail)
        
    return crud.add_user(details,db)
    


@router.put("/{id}")
def update_user_by_id(id:int,updated_details:user.UpdateUser,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    return crud.update_user_by_id(id,updated_details,db)


@router.delete("/{id}")
def delete(id:int,db:Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    return crud.delete_user(id,db)

@router.get("/page",response_model=Page[user.UserOut])
def get_page(param: Params=Depends(), db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    res=crud.get_all_users(db)


    return paginate(res,param)

@router.get("/{id}",response_model=user.UserOut)
def get_user_by_id(id:int,db: Session=Depends(get_db),get_current_user: TokenData=Depends(oauth2.get_current_active_user)):
    return crud.get_user_by_id(id,db)