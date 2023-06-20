from fastapi import Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
from blogs import schemas, models


def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(req:schemas.Blog, db:Session):
    new_blog = models.Blog(title=req.title,body=req.body, user_id =1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy(id:int, db:Session):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

def update(id:int, req:schemas.Blog, db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'not found {id}')
    blog.update(req.dict())
    db.commit()
    return 'updated'

def get_by_id(id:int,response:Response,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with id {id} not found'}
    return blogs