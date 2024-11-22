import os
from typing import Dict, Union, List

from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
import requests

import app.models as models
from app.schemas.users import User

LIMEWARE_API_KEY = os.getenv("JWT_SECRET_KEY", "should-be-an-environment-variable")

def gen_image(prompt):
    url = "https://api.limewire.com/api/image/generation"

    payload = {
    "prompt": prompt,
    "aspect_ratio": "1:1"
    }

    headers = {
    "Content-Type": "application/json",
    "X-Api-Version": "v1",
    "Accept": "application/json",
    "Authorization": LIMEWARE_API_KEY
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    
    return data