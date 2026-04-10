from pydantic import BaseModel

class usercreate(BaseModel):
    name:str
    email:str
    password:str

class userlogin(BaseModel):
    email:str
    password:str   
class userupdate(BaseModel):
    name:str
    email:str
    password:str    
class userresponse(BaseModel):
    id:int
    name:str
    email:str
    class Config:
        orm_mode=True

class loginresponse(BaseModel):
    id:int
    name:str
    email:str
    message:str
    class Config:
        orm_mode=True
