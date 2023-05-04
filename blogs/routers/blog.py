from fastapi import APIRouter, Depends, HTTPException, Response ,status
import schemas, database, models
from database import SessionLocal
from sqlalchemy.orm import Session
from repository import blog

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)
get_db = database.get_db

@router.get('/get',response_model=list[schemas.ShowBlog])
def get_all(db:SessionLocal = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(req:schemas.Blog, db:Session = Depends(get_db)):
    return  blog.create(req,db)

@router.get('/getby{id}',status_code=200, response_model=schemas.ShowBlog)
def get_by_id(id:int,response:Response,db:Session = Depends(get_db)):
    return blog.get_by_id(id,db)

@router.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_by_id(id:int,db:Session = Depends(get_db)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int, req:schemas.Blog, db:Session = Depends(get_db)):
    return blog.update(id,req,db)


