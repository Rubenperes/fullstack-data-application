from fastapi import FastAPI
import datetime
from pydantic import BaseModel
import routers

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}

#1
@app.get("/current-date")
def get_current_date():
    return {"date": datetime.datetime.now().strftime("%d-%m-%Y")}

#2
class Book(BaseModel):
    name: str
    author : str
    publication_year: int

#3 = models/database.py

#4 = models/post.py

#5
app.include_router(routers.PostRouter)