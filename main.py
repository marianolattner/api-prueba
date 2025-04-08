from fastapi import FastAPI
from routers import products,users,jwt_auth_users,basic_auth_users, users_db
from fastapi.staticfiles import StaticFiles
app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(jwt_auth_users.router)
app.include_router(basic_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola fastAPI"

@app.get("/url")
async def url():
    return { "url":"https://www.youtube.com/watch?v=_y9qQZXE24A&t=6524s&ab_channel=MoureDevbyBraisMoure" }