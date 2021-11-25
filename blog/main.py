from blog.routers import authentication
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
from .routers import blog, user, authentication, file, book

app = FastAPI()

# static file setup config
app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(file.router)
app.include_router(book.router)
