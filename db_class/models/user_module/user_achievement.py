from __future__ import annotations

from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base_class import Base


class UserAchievement(Base):
    __tablename__ = "user_achievements"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    achievements_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("achievements.id", ondelete="CASCADE"),
        primary_key=True,
    )

    user: Mapped[object] = relationship(
        "User",
        back_populates="achievements",
    )
    achievement: Mapped[object] = relationship(
        "Achievement",
        back_populates="user_achievements",
    )
