from typing import List

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    login_date: str
    device_token: str
    device_id: int
    id: int
    created: str
    is_active: bool
    class Config:
        orm_mode = True
        
class User(BaseModel):
    id: int
    email: str
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    email: str
    password: str
    




    