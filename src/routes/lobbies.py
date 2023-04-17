# from typing import List
#
from fastapi import APIRouter, Depends
# from sqlalchemy.orm import Session
#
# from src.config.database import get_session
# from src.data.models import sample

router = APIRouter(prefix='/api/lobbies', tags=['Lobbies'])


@router.post('/')
async def create_lobby():
    pass
#
#
# @router.get("/")
# async def list_stores(
#         db_session: Session = Depends(get_session),
# ):
#     return db_session.query(sample.Store).all()
