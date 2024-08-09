from sqlalchemy import select, delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.interfaces.repo import IShortURLRepo
from src.infrastructure.database.models import ShortURL
from src.core.models.dto import ShortURLDTO
from .base import BaseRepo


class ShortURLRepo(IShortURLRepo, BaseRepo[ShortURL]):

    def __init__(self, session: AsyncSession):
        super().__init__(model=ShortURL, session=session)

    async def create_short_url(self, url: ShortURLDTO) -> ShortURLDTO:
        stmt = (
            insert(self.model)
            .values(
                {
                    'user_id': url.user_id,
                    'original_url': url.original_url,
                    'small_url': url.short_url
                }
            )
            .returning(self.model)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_dto()

    async def get_original_url(self, short_url: str) -> ShortURLDTO:
        stmt = (
            select(self.model)
            .where(self.model.short_url == short_url)
        )
        res = await self.session.execute(stmt)
        return res.scalar_one().to_dto()

    async def get_user_links(self, user_id: int) -> list[ShortURLDTO]:
        stmt = (
            select(self.model)
            .where(self.model.user_id == user_id)
        )
        res = await self.session.execute(stmt)
        return [link.to_dto() for link in res.scalars().all()]

    async def delete_link(self, short_url: str):
        stmt = (
            delete(self.model)
            .where(self.model.short_url == short_url)
        )
        await self.session.execute(stmt)
