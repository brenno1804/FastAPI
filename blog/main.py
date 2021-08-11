from fastapi import FastAPI
from . import models, database
from .router import blog, user


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
models.Base.metadata.create_all(bind=database.engine)
