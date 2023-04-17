#
from fastapi import APIRouter

router = APIRouter(prefix='/api/arsenals', tags=['Lobbies'])


@router.post('/')
async def create_arsenal(

):
    pass
