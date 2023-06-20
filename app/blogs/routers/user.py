from fastapi import APIRouter , Depends, HTTPException ,status

from blogs.hashing import Hash
from sqlalchemy.orm import Session
from blogs.repository import user
from blogs import schemas, models, database

router = APIRouter(
    prefix="/user",
    tags=['User']
)

get_db = database.get_db

@router.post('/', response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}', response_model= schemas.ShowUser)
def get_user_by_id(id:int,db:Session = Depends(get_db)):
    return user.get_user_by_id(id,db)