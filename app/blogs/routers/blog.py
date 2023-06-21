from fastapi import APIRouter, Depends, HTTPException, Response ,status
import blogs.schemas, blogs.database
from blogs.Oauth2 import get_current_user
from blogs.database import SessionLocal
from sqlalchemy.orm import Session
import blogs.database
from blogs.repository import blog
from blogs import database, schemas

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/get',response_model=list[schemas.ShowBlog])
def get_all(db:SessionLocal = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(req:schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return  blog.create(req,db)

@router.get('/getby{id}',status_code=200, response_model=schemas.ShowBlog)
def show(id:int,response:Response,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.show(id,db)

@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, req:schemas.Blog, db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.update(id,req,db)


