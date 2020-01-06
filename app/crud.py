from sqlalchemy.orm import Session

from . import models, pydantic_schemas


def create_user(db: Session, user: pydantic_schemas.UserCreate):
    password = user.password
    email = user.email
    new_user = models.User(email=email,password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user