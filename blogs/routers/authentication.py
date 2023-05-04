
import tokens
from fastapi import APIRouter, Depends , HTTPException, status
import schemas , database, models
from sqlalchemy.orm import Session
from hashing import Hash

router = APIRouter(
    tags=["authentication"]
)

@router.post('/login')
def login(req:schemas.login, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid credentials")
    if not Hash.verify(user.password, req.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid credentials")
    
    access_token = tokens.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}