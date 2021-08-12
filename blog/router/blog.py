from fastapi import APIRouter, Depends, status
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
    )


@router.get('/',
            status_code=status.HTTP_200_OK,
            response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db),
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,
           db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.Blog)
def get(id: int,
        db: Session = Depends(database.get_db),
        current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int,
           request: schemas.Blog,
           db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int,
           db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db)
