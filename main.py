from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {'data': f'{limit} published blogs blogs from database '}
    else:
        return {'data': f'{limit} blogs blogs from database '}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}


@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):

    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog():
    return {'data': "Blog is created"}
