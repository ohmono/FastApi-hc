from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends
from controllers import user
import schemas
from DB import database


router = APIRouter(prefix="/user", tags=['users'])

# create user


@router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(req: schemas.User, db: Session = Depends(database.get_db)):
    return user.create(req, db)
# get 1 user


@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return user.get(id, db)
