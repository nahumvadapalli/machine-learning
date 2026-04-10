from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session 
from database import engine,Base,get_db
import models,schemas
import bcrypt
Base.metadata.create_all(bind=engine)
app=FastAPI()

@app.post("/Create",response_model=schemas.userresponse,tags=["Create"])
def create_user(user:schemas.usercreate,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.email==user.email).first()
    
    if db_user:
        raise HTTPException(status_code=400,detail="Email already exists")
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    new_user=models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@app.post("/Login",response_model=schemas.loginresponse,tags=["Login"])
def Login_user(user:schemas.userlogin,db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.email==user.email).first()
    if not db_user:
        raise HTTPException(status_code=400,detail="Invalid email")
    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.password):
        raise HTTPException(status_code=400,detail="Invalid password")
    return {"id": db_user.id, "name": db_user.name, "email": db_user.email, "message": "Login successful"}
@app.get("/GetUsers",response_model=list[schemas.userresponse],tags=["GetUsers"])
def list_users(db:Session=Depends(get_db)):
    db_users=db.query(models.User).all()
    return db_users
@app.get("/GetUser/{user_id}",response_model=schemas.userresponse,tags=["GetUser"])
def get_user(user_id: int, db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    return db_user
@app.put("/UpdateUser/{user_id}",response_model=schemas.userupdate,tags=["UpdateUser"])
def update_user(user_id: int, user:schemas.userupdate, db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    db_user.name=user.name
    db_user.email=user.email
    db_user.password=user.password
    db.commit()
    db.refresh(db_user)
    return db_user
@app.delete("/DeleteUser/{user_id}",tags=["DeleteUser"])
def delete_user(user_id: int, db:Session=Depends(get_db)):
    db_user=db.query(models.User).filter(models.User.id==user_id).first()
    if not db_user:
        raise HTTPException(status_code=404,detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}