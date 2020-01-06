import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from . import models, pydantic_schemas

from .database import SessionLocal, engine
from .crud import create_user
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.graphql_schemas import schema


app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


app.add_route("/", GraphQLApp(schema=schema)) 




@app.post("/user/", response_model=pydantic_schemas.User)
def _create_user(user:pydantic_schemas.UserCreate, db: Session = Depends(get_db)):
    response = create_user(db, user)
    return response
    