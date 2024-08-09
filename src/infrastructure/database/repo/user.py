from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.database.models import User
from src.core.interfaces.repo import IUserRepo
from src.core.models.dto import UserDTO
from .base import BaseRepo


class UserRepo(IUserRepo, BaseRepo[User]):

    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def create_user(self, user: UserDTO) -> UserDTO:
        stmt = (
            insert(self.model)
            .values(
                {
                    'user_id': user.user_id,
                    'login': user.login,
                    'email': user.email,
                    'password_hash': user.password_hash,
                    'password_salt': user.password_salt
                }
            )
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_dto()

    async def get_by_user_id(self, user_id: int) -> UserDTO:
        stmt = (
            select(self.model)
            .where(self.model.user_id == user_id)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_dto()

    async def get_by_email(self, email: str) -> UserDTO:
        stmt = (
            select(self.model)
            .where(self.model.email == email)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_dto()