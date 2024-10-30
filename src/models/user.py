from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app import db


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    api_key: Mapped[str] = mapped_column()
