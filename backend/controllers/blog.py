from fastapi import HTTPException, status, Depends
import models


def create(req, db, current_user):
    new_blog = models.Blog(title=req.title, body=req.body,
                           user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id, req, db, current_user):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with the id {id} not found')
    blog = blog.filter(models.Blog.user_id == current_user.id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with the id {id} its not your')
    blog.update(vars(req))
    db.commit()
    return 'done'


def delete(id, db, current_user):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with the id {id} not found')
    blog = blog.filter(models.Blog.user_id == current_user.id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'blog with the id {id} its not your')
    blog.delete(synchronize_session=False)
    db.commit()
    return 'done'


def get_all(db):
    blogs = db.query(models.Blog).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'not blogs found')
    return blogs


def get(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with the id {id} is not available')
    return blog


def get_all_user(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with the id {id} is not available')

    blogs = db.query(models.Blog).filter(models.Blog.user_id == id).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'not blogs found')
    return blogs
