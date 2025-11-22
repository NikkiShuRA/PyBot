from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Integer, Text, Boolean, ForeignKey, Date


class Base(DeclarativeBase):
    pass
