from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.models as models
from app.services.gen_img import gen_image
from app.schemas.images import Image

gen_img_router = APIRouter(prefix="/gen-img")

@gen_img_router.post("/", tags=["gen-img"])
async def generate_image(image : Image):
        return gen_image(image.prompt)
