import os
from typing import Dict, Union, List

from fastapi import Depends, HTTPException, Header
from sqlalchemy.orm import Session
import requests

import app.models as models
from app.schemas.users import User

LIMEWARE_API_KEY = os.getenv("LIMEWARE_API_KEY")

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
    "Authorization": f"Bearer {LIMEWARE_API_KEY}"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    data = response.json()
    
    print(f"data : {data}")
    
    return data