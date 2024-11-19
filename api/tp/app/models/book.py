from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class Book(BaseSQL):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publication_year = Column(DateTime)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())
