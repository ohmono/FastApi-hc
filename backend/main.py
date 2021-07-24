from DB.database import engine
import models
from security import oauth2
import schemas
from fastapi import FastAPI, Depends
from routers import blog, user, auth

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)


# @app.get("/users/me", tags=['get user id'])
# async def read_users_me(current_user: schemas.UserId = Depends(oauth2.get_current_user)):
#     return current_user

# @app.get('/')
# def hola():
#    return {'response': 'correct'}

# if __name__ == '__main__':
#    uvicorn.run(app, host='127.0.0.1', port='9000')
