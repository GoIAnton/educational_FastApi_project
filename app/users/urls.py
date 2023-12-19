from fastapi import APIRouter
import os

router = APIRouter()


@router.get("/users/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/")
async def index():
    return {"page": os.getcwd()}
