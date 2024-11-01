from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from app.models.base import Base


class Pizza(Base):
    __tablename__ = "tours"

    id: Mapped[int] = mapped_column("id", primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    price: Mapped[float] = mapped_column()