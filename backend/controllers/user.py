from fastapi import HTTPException, status
from security.hashing import Hash
import models


def create(req, db):
    new_user = models.User(name=req.name, email=req.email,
                           password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get 1 user


def get(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')
    return user
