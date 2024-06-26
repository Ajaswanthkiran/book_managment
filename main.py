

from fastapi import FastAPI,Depends

from book_app.routers.book import router

app=FastAPI()


app.include_router(router)

