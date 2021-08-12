from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, database, models, token
from sqlalchemy.orm import Session
from ..hashing import Hash


router = APIRouter(
    tags=['Authentication'],
    prefix='/login'
    )


@router.post('/',
             status_code=status.HTTP_201_CREATED)
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).\
           filter(models.User.email == request.username).\
           first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not Found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Incorrect Password')

    access_token = token.create_access_token(data={"sub": user.email})

    return access_token
