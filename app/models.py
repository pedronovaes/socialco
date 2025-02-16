"""
This module handles the database models from the application. Each database
will be represented by a collection of classes. THe ORM layer within
SQLAlchemy store in __init__ file will do the translations required to map
objects create from these classes into rows in the proper database tables.
"""

from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        index=True,
        unique=True
    )
    email: so.Mapped[str] = so.mapped_column(
        sa.String(64),
        index=True,
        unique=True
    )
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return f"<User {self.username}>"
