

from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer


from book_app.schemas.token import TokenData
from book_app.services.token import verify_token



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str =Depends(oauth2_scheme)):
    print("uuuuuuuuuuui")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token,credentials_exception)
    
async def get_current_active_user(current_user: TokenData = Depends(get_current_user)):
    if current_user.role != "user":
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return current_user

async def get_current_active_author(current_user: TokenData = Depends(get_current_user)):
    print("came here")
    if current_user.role != "author":
        raise HTTPException(status_code=400, detail="Not enough permissions")
    print(current_user)
    return current_user

async def get_current_active_publisher(current_user: TokenData = Depends(get_current_user)):
    if current_user.role != "publisher":
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return current_user