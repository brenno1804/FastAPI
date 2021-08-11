from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
    )


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowUserContent)
def get(id: int, db: Session = Depends(database.get_db)):
    return user.show(id, db)


@router.post('/',
             status_code=status.HTTP_201_CREATED,
             response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)
