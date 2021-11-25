from blog.routers import authentication
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from . import models
from .database import engine
<<<<<<< HEAD
from .routers import blog, user, authentication, file, book
=======
from .routers import blog, user, authentication, file, test
>>>>>>> 466b38d0d270bf09a90e784a5c75a064896ec3f3

app = FastAPI()

# static file setup config
app.mount("/static", StaticFiles(directory="static"), name="static")

models.Base.metadata.create_all(engine)


app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(file.router)
<<<<<<< HEAD
app.include_router(book.router)
=======
app.include_router(test.router)
>>>>>>> 466b38d0d270bf09a90e784a5c75a064896ec3f3
