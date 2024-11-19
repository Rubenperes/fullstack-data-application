from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.db import get_db
from api.tp.app.models.book import Book

router = APIRouter(prefix="/books")

@router.get("/", tags=["books"])
async def get_all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
