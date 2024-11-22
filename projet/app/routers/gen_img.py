from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.models as models
from app.services.gen_img import gen_image

gen_img_router = APIRouter(prefix="/gen-img")

@gen_img_router.get("/", tags=["gen-img"])
async def generate_image(prompt):
        return gen_image(prompt)
    