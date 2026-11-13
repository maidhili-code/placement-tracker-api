
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
from typing import Optional

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String, nullable=False
    )

    applications = relationship(
        "Application", back_populates="owner"
    )


class Application(Base):
    __tablename__ = "applications"

    app_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    company: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(
        String, nullable=False, default="applied"
    )

    user_id: Mapped[Optional[int]] = mapped_column(
    ForeignKey("users.id"), nullable=True
)

    owner = relationship("User", back_populates="applications")
