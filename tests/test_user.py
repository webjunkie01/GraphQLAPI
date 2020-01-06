import sys
sys.path.append(".")
import pytest
from sqlalchemy.orm import Session
from app.crud import *
from app.models import *

from app.database import SessionLocal, engine
import json
from fastapi.encoders import jsonable_encoder


#models.Base.metadata.create_all(bind=engine)


def test_create_user():
    payload = pydantic_schemas.UserCreate(email='memo@memo.com', password= '123')
    result = create_user(SessionLocal(), payload)
    assert result is not None