from pydantic import BaseModel


class Image(BaseModel):
    prompt: str
