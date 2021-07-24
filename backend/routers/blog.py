
from controllers import blog
import schemas
from DB import database
from security import oauth2
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, status, Depends

router = APIRouter(prefix='/blog', tags=['blogs'])


# create blog
@router.post('', status_code=status.HTTP_201_CREATED)
def create_blog(req: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(req, db, current_user)

# update blog


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update_blog(id: int, req: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, req, db, current_user)

# delete 1 blog


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete(id, db, current_user)


# get all blogs
@router.get('', status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

# get 1 blog


@router.get('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(database.get_db)):
    return blog.get(id, db)

# get all user blogs


@router.get('/user/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=List[schemas.ShowBlog])
def get_all_user_blogs(id: int, db: Session = Depends(database.get_db)):
    return blog.get_all_user(id, db)
