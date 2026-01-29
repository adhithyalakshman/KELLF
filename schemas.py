from sqlalchemy  import create_engine,Column,Integer,String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine=create_engine("sqlite:///database.db")
session=sessionmaker(bind=engine)
Base=declarative_base()

def getdb():
    return session

class User(Base):
    __tablename__ = 'users'
    id=C




