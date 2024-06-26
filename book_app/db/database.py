

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext import declarative
from dotenv import load_dotenv
from sqlalchemy import MetaData
import os

load_dotenv()

connection_url=os.environ.get("url")
Base=declarative.declarative_base()


engine=create_engine(connection_url,echo=True)

Session=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    session=Session()
    try:
        yield session
    finally:
        session.close()





