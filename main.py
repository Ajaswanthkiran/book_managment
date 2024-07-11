

from fastapi import FastAPI,Depends, HTTPException,Request,status

from fastapi.responses import JSONResponse
import uvicorn
from book_app.routers.book import router as book_router

from book_app.routers.author import router as author_route

from book_app.routers.publisher import router as publisher_route

from book_app.routers.login import router as login
from book_app.routers.user import router as user_router
from book_app.services.token import verify_token
 

app=FastAPI()

@app.middleware("http")
async def authorization(request: Request, call_next):
    
  
    try:
        if request.url.path in ['/login','/docs','/openapi.json']:
            response = await call_next(request)
            return response
        else:
            credentials_exception = HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
            
            if "Authorization" not in request.headers:
                raise HTTPException(status_code=404, detail="Authorization Header not found")
            else:
                token=request.headers["Authorization"]
                verification_of_token=verify_token(token,credentials_exception)
                if verification_of_token:
                    response = await call_next(request)
                    return response
                else:
                    return JSONResponse(status_code=403,content={"reason":"Validation failed"}) # or 401
    except Exception as er:
        return JSONResponse(status_code=401,content={'reason': str(er)})
    
 
    

app.include_router(login)
app.include_router(book_router)
app.include_router(author_route)
app.include_router(publisher_route)
app.include_router(user_router)



if __name__=="__main__":
    uvicorn.run("main:app",reload=True)