from fastapi import FastAPI
from typing import Optional
from . import schemas

app = FastAPI()


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


@app.post('/blog')
def create_blog(blog: schemas.Blog):
    return {'data': f'Blog is created with title as {blog.title}'}
