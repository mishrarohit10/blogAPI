from fastapi.security import OAuth2PasswordRequestForm
from blogs import token
from fastapi import APIRouter, Depends , HTTPException, status
from blogs import schemas , database, models
from sqlalchemy.orm import Session
from blogs.hashing import Hash

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(req:OAuth2PasswordRequestForm = Depends(), db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid credentials")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid credentials")
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}