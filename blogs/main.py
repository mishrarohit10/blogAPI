from fastapi import FastAPI, Depends , status , Response, HTTPException
from sqlalchemy.orm import Session
from routers import blog, user, authentication
import schemas , models 
from database import engine, get_db
from hashing import Hash
from sqlalchemy.orm import Session

# import uvicorn
# if __name__ == "__main__":# #uvicorn.run(app, host = "127.0.0.1" ,port = 9000)  custom port 

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post('/blog', status_code=status.HTTP_201_CREATED, tags=["Blog"])
# def create(req:schemas.Blog, db:Session = Depends(get_db)):
#     new_blog = models.Blog(title=req.title,body=req.body, user_id =1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/get',response_model=list[schemas.ShowBlog], tags=["Blog"])
# def get_all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# @app.get('/getby{id}',status_code=200, response_model=schemas.ShowBlog, tags=["Blog"])
# def get_by_id(id:int,response:Response,db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Blog with id {id} not found')
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail':f'Blog with id {id} not found'}
#     return blogs


# @app.delete('/blogs/delete/{id}',status_code=status.HTTP_204_NO_CONTENT, tags=["Blog"])
# def delete_by_id(id:int,db:Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "done"


# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED, tags=["Blog"])
# def update(id:int, req:schemas.Blog, db:Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'not found {id}')
#     blog.update(req.dict())
#     db.commit()
#     return 'updated'

# @app.post('/user', response_model=schemas.ShowUser, tags=["User"])
# def create_user(request:schemas.User,db:Session = Depends(get_db)):
#     new_user = models.User(name = request.name,email=request.email,password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}', response_model= schemas.ShowUser, tags=["User"])
# def get_user_by_id(id:int,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found")
#     return user












 

