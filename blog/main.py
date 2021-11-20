from blog.routers import authentication
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
from .routers import blog, user, authentication

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
