from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.database.models.base import Base, TimestampMixin
from src.core.models.dto import ShortURLDTO


class ShortURL(Base, TimestampMixin):
    __tablename__ = 'short_links'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True, index=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), nullable=False, index=True)
    original_url: Mapped[str] = mapped_column(String(2000))
    short_url: Mapped[str] = mapped_column(String(8), unique=True, index=True)

    user = relationship("User", back_populates="shortened_urls")

    def to_dto(self) -> ShortURLDTO:
        return ShortURLDTO.model_validate(self)
