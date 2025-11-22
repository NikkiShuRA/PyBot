from __future__ import annotations

from typing import List, Optional

from sqlalchemy import BigInteger, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base_class import Base


class Level(Base):
    __tablename__ = "levels"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)
    required_points: Mapped[int] = mapped_column(Integer, nullable=False)

    users: Mapped[List[object]] = relationship(
        "User",
        back_populates="level",
    )
