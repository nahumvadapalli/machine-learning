from pydantic import Basemodel
class studentcreate(Basemodel):
    name:str
    age:int
    grade:str
class studentresponse(Basemodel):
    id:int
    name:str
    age:int
    grade:str