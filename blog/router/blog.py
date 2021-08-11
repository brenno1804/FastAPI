from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
    )


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_new_blog(request: schemas.Blog,
                    db: Session = Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.delete(synchronize_session=False)
    db.commit()
    return {'data': f'Blog with id {id} deleted'}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int,
                request: schemas.Blog,
                db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found')
    blog.update(request, synchronize_session=False)
    db.commit()
    return {'data': f'Blog with id {id} updated'}


@router.get('/{id}',
            status_code=status.HTTP_200_OK,
            response_model=schemas.ShowBlog)
def get_blog(id: int,
             response: Response,
             db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} is not available')
    return blog
