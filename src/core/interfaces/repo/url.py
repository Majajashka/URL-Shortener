from abc import ABC, abstractmethod

from src.core.models.dto import ShortURLDTO


class IShortURLRepo(ABC):
    @abstractmethod
    async def get_original_url(self, shortened_url: str) -> ShortURLDTO:
        pass

    @abstractmethod
    async def create_short_url(self, original_url: str) -> ShortURLDTO:
        pass

    @abstractmethod
    async def get_user_links(self, user_id: int) -> ShortURLDTO:
        pass

    @abstractmethod
    async def delete_link(self, shortened_url: str) -> ShortURLDTO:
        pass
