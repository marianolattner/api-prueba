from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#Inicio el server con uvicorn main:router --reload
router = APIRouter()

#Entidad User

class User(BaseModel):
    id: int
    name: str 
    surname: str
    nickname: str
    age: int 

users_list = [User(id=1,name="Mariano",surname ="Lattner",nickname="mana",age=26),
              User(id=2,name="Mariam",surname ="Bakir",nickname="maroxita",age=25),
              User(id=3,name="Juan Domingo",surname ="Peron",nickname="el primer trabajador",age=420)]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Mariano", "surname": "Lattner", "nickname": "mana", "age": 26},
            {"name": "Mariam", "surname": "Bakir", "nickname": "maroxita", "age": 25},
            {"name": "Gaara", "surname": "Bakir", "nickname": "kitipo", "age": 4},
            {"name": "Rihana", "surname": "Lattner", "nickname": "rurru", "age": 5}]

@router.get("/users")
async def users():
    return users_list

#path -- lo usamos cuando practicamente es un parametro obligatorio (algo fijo)
@router.get("/user/{id}")
async def user(id:int):
    return search_user(id)

#query -- lo usamos cuando es un parametro no necesario para hacer la peticion  (algo cambiante por cada usuario x ej)
@router.get("/user/")
async def user(id:int):
    return search_user(id)

    

@router.post("/user/", status_code=201)
async def user(user:User):
    if type(search_user(user.id))== User:
        raise HTTPException(status_code=204, detail="El usuario ya existe")
    else:
        users_list.routerend(user)
        return user

@router.put("/user/")
async def user(user:User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"Error":"No se ha podido actualizar el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user(id:int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"Error":"No se ha podido eliminar el usuario"}



def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list )
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el usuario"}