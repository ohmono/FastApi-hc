from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from DB import database

from controllers import auth
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter(tags=['authentications'])


@router.post('/login')
def login(req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth.login(req, db)
