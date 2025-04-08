from fastapi import APIRouter

router = APIRouter(prefix="/products", # Prefijo porque todas vienen del mismo path
                   tags=["products"], # Tag para agrupar en la documentacion
                   responses={404:{"message": "No encontrado"}})  # Respuesta cuando falla 

products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]