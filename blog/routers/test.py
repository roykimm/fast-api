from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models
from ..hashing import Hash
from ..repository import user
import subprocess
import os

router = APIRouter(
    prefix='/test',
    tags=['TEST'],
)

@router.post('/')
async def get_test(request : schemas.test):
    s = request.code
    print(request.code)
    a = exec(s)
    print(a)
    output = subprocess.getstatusoutput(s)
    print(output)
    return "hi"