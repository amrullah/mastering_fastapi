from passlib.context import CryptContext
from sqlalchemy.orm import Session

from db.models import User
from schemas import UserBase


pwd_cxt = CryptContext(schemes='bcrypt', deprecated='auto')

class Hash():
    def bcrypt(self, password: str):
        return pwd_cxt.hash(password)

    def verify(self, hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)


def create_user(db: Session, request: UserBase):
    new_user = User(
        email=request.email,
        username=request.username,
        password=Hash().bcrypt(request.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
