

from fastapi import FastAPI,Depends

import uvicorn
from book_app.routers.book import router as book_router

from book_app.routers.author import router as author_route

from book_app.routers.publisher import router as publisher_route

app=FastAPI()


app.include_router(book_router)
app.include_router(author_route)
app.include_router(publisher_route)

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)