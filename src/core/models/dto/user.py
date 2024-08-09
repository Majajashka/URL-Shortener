from pydantic import EmailStr

from .base import BaseDTO


class UserDTO(BaseDTO):
    user_id: int
    login: str
    email: EmailStr
    password_hash: bytes
    password_salt: bytes
