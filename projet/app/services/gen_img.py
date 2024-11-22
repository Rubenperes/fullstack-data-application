import os
from typing import Dict, Union, List

from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
import requests
import time

import app.models as models
from app.schemas.users import User

STARRYAI_API_KEY = os.getenv("STARRYAI_API_KEY")

def get_image(id):
    url = f"https://api.starryai.com/creations/{id}"

    headers = {
        "accept": "application/json",
        "X-API-Key": STARRYAI_API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()

def gen_image(prompt):
    url = "https://api.starryai.com/creations/"

    payload = {
        "model": "lyra",
        "aspectRatio": "square",
        "highResolution": False,
        "images": 1,
        "steps": 20,
        "initialImageMode": "color",
        "prompt": prompt
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-Key": STARRYAI_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()

    id = data["id"]

    response = get_image(id)

    status = response["status"]

    print(f"status : {status}")

    while status != "completed":
        time.sleep(25)
        response = get_image(id)
        status = response["status"]
        print(f"status : {status}")

    print(response)

    url = response["images"][0]["url"]

    print(f"url : {url}")

    return url