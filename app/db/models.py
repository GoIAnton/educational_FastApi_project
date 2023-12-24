from sqlalchemy import (
    Integer, String,
    Column, DateTime,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Post(Base):
    __tablename__ = 'posts'
    id = Column(
        Integer,
        primary_key=True,
    )
    title = Column(
        String(100),
        nullable=False,
    )
    content = Column(
        String(50),
        nullable=False,
    )
    created_on = Column(
        DateTime(),
        default=datetime.now,
    )
    updated_on = Column(
        DateTime(),
        default=datetime.now,
        onupdate=datetime.now,
    )

    __table_args__ = (
        UniqueConstraint('title'),
    )
