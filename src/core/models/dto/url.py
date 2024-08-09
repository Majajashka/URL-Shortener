from .base import BaseDTO


class ShortURLDTO(BaseDTO):
    user_id: int
    original_url: str
    short_url: str
