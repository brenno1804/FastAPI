from fastapi import FastAPI
from . import models, database
from .router import blog, user, authentication


app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
models.Base.metadata.create_all(bind=database.engine)
