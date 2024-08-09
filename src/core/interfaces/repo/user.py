from abc import ABC, abstractmethod

from src.core.models.dto import UserDTO


class IUserRepo(ABC):
    @abstractmethod
    async def get_by_user_id(self, user_id: int) -> UserDTO:
        pass

    @abstractmethod
    async def get_by_email(self, email: str) -> UserDTO:
        pass

    @abstractmethod
    async def create_user(self, user) -> UserDTO:
        pass

