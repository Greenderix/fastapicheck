from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.config.database import get_session
from src.data.models.user import User
from src.data.schemas.users import CreateUser

router = APIRouter(prefix='/api/users', tags=['Users'])


@router.post('/')
async def create_user(
        user: CreateUser,
        session: Session = Depends(get_session)
):
    hashed_password = user.password + "sosijopu"
    user_ = User(
        username=user.username,
        hashed_password=hashed_password
    )
    session.add(user_)
    session.commit()


@router.get("/")
async def get_all_users(
        session: Session = Depends(get_session)
):
    return session.query(User).all()


@router.get("/{user_id:int}")
async def get_user_by_id(
        user_id: int,
        session: Session = Depends(get_session)
):
    return session.query(User).filter(User.id == user_id).first()


@router.delete("/{user_id:int}")
async def delete_user_by_id(
        user_id: int,
        session: Session = Depends(get_session)
):
    return session.query(User).filter(User.id == user_id).delete()
