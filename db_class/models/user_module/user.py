from __future__ import annotations

from datetime import date
from typing import List, Optional

from sqlalchemy import BigInteger, Integer, Text, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base_class import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(Text, nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(Text)
    patronymic: Mapped[Optional[str]] = mapped_column(Text)
    phone_number: Mapped[Optional[str]] = mapped_column(Text)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    github_url: Mapped[Optional[str]] = mapped_column(Text)
    join_date: Mapped[Optional[date]] = mapped_column(Date)

    activity_status_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("user_activity_statuses.id"),
    )
    points: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    level_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("levels.id"),
    )
    academic_role_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("academic_roles.id"),
    )
    admin_role_id: Mapped[Optional[int]] = mapped_column(
        BigInteger,
        ForeignKey("admin_roles.id"),
    )


    activity_status: Mapped[Optional[object]] = relationship(
        "UserActivityStatus",
        back_populates="users",
    )
    level: Mapped[Optional[object]] = relationship(
        "Level",
        back_populates="users",
    )
    academic_role: Mapped[Optional[object]] = relationship(
        "AcademicRole",
        back_populates="users",
    )
    admin_role: Mapped[Optional[object]] = relationship(
        "AdminRole",
        back_populates="users",
    )

    competencies: Mapped[List[object]] = relationship(
        "UserCompetence",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    achievements: Mapped[List[object]] = relationship(
        "UserAchievement",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    valuations_received: Mapped[List[object]] = relationship(
        "Valuation",
        foreign_keys="Valuation.recipient_id",
        back_populates="recipient",
    )
    valuations_given: Mapped[List[object]] = relationship(
        "Valuation",
        foreign_keys="Valuation.giver_id",
        back_populates="giver",
    )
