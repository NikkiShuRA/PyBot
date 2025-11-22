from __future__ import annotations

from sqlalchemy import BigInteger, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base_class import Base


class UserCompetence(Base):
    __tablename__ = "user_competencies"

    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    competence_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey("competencies.id", ondelete="CASCADE"),
        primary_key=True,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    user: Mapped[object] = relationship(
        "User",
        back_populates="competencies",
    )
    competence: Mapped[object] = relationship(
        "Competence",
        back_populates="user_competencies",
    )
