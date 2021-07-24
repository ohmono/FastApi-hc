from fastapi import HTTPException, status
from security.hashing import Hash
from security import JWToken
import models


def login(req, db):
    user = db.query(models.User).filter(
        models.User.email == req.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credentials')

    if not Hash.verify(req.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Invalid Credentials')
    sub = str(user.id)
    access_token = JWToken.create_access_token(data={"sub": sub})
    return {"access_token": access_token, "token_type": "bearer"}
