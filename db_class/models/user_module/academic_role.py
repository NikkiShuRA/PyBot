from __future__ import annotations

from typing import List, Optional

from sqlalchemy import BigInteger, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...base_class import Base


class AcademicRole(Base):
    __tablename__ = "academic_roles"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    users: Mapped[List[object]] = relationship(
        "User",
        back_populates="academic_role",
    )
