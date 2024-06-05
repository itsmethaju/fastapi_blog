from pydantic import BaseModel
from typing import Optional

class blog(BaseModel):
    id: int
    video_url: str
    description: str
    title: str

class Work(BaseModel):
    id: int
    img_url: str
    description: str
    title: str
    
class Team(BaseModel):
    id: int
    img_url: str
    description: str
    title: str
    
class Contact(BaseModel):
    id: int
    name: str
    email: str
    company: str
    query: str
    
    
