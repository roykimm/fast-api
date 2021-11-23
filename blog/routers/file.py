from typing import List
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter, UploadFile, File
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2
import shutil
import secrets
from fastapi.staticfiles import StaticFiles
from PIL import Image
import os


router = APIRouter(
    prefix="/file",
    tags=['Files'],
)
get_db = database.get_db


@router.post('/')
async def file(file: UploadFile = File(...)):

    with open(f'{file.filename}', "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_name": file.filename}


@router.post('/img')
async def upload_image(files: List[UploadFile] = File(...)):

    for img in files:
        with open(f'{img.filename}', "wb") as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"file_name": "Good"}

# image Upload하기


@router.post("/uploadfile/profile")
async def create_upload_file(file: UploadFile = File(...), current_user: schemas.User = Depends(oauth2.get_current_user)):

    FILEPATH = os.getcwd() + "/static/images/"
    filename = file.filename
    # test.png > ["test", "png"]
    extension = filename.split(".")[1]

    if extension not in ["png", "jpeg", "jpg"]:
        return {"detail": "file extension not allowed"}

    # ex) /static/images/udfe23j3jk.png
    token_name = secrets.token_hex(10) + "." + extension
    generated_name = FILEPATH + token_name
    file_content = await file.read()

    print(f"token_name : {token_name}")
    print(f"generated_name : {generated_name}")

    with open(generated_name, "wb") as file:
        file.write(file_content)

        # PILLOW
        img = Image.open(generated_name)
        img = img.resize(size=(200, 200))
        img.save(generated_name)

        file.close()

    return {}
    # return {"status" : "ok", "filename" : file_url}

    # business = await Business.get(owner=user)
    # owner = await business.owner

    # if owener == user:
    #     business.logo = token_name
    #     await business.save()
    # else:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND, detail=f"blog id {id} not found")


# @router.get('/', response_model=List[schemas.ShowBlog])
# def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
#     return blog.get_all(db)
