from sqlalchemy import Column, Integer, String
from database from database import Base

class students(Base):
    __tablename__="students"
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String)
    age=Column(Integer)
    grade=Column(String)