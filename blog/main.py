from fastapi import FastAPI, Depends
from typing import Optional
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


@app.get('/')
def get_main_page():
    return {'data': 'Welcome to my FastAPI Test'}


@app.get('/blog')
def get_list_of_blogs(limit: int = 10,
                      published: bool = True,
                      sort: Optional[str] = None):
    return {
        'data': {
            'title': f'Get {limit} and published={published} blogs',
            'blog': ['unpublished blogs']
        }
    }


@app.get('/blog/unpublished')
def get_unpublished_blogs():
    return {'data': {'blog': ['unpublished blogs']}}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'data': {'blog': id}}


@app.get('/blog/{id}/comments')
def get_blog_comments(id: int):
    return {'data': {'blog': id, 'comments': ['comments list']}}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog')
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
