from fastapi import APIRouter

from db.db_controller import engine
from db.models import Post
from sqlalchemy.orm import Session

router = APIRouter()


session = Session(bind=engine)
p1 = Post(
    title='Post1',
    content='Text1',
)
session.add(p1)
session.commit()


@router.get("/")
async def index():
    data = session.query(Post).all()
    return [{'data': data, }]
