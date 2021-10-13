from fastapi import APIRouter

from config.database import collection_repuestos
from models.repuesto_model import Repuesto

from schemas.repuestos_schemas import repuestoEntity, repuestosEntity
from bson import ObjectId

repuesto = APIRouter()


# Mostrando Todos los Repuestos
@repuesto.get("/repuestos", response_model=list[Repuesto])
async def find_all_repuestos():
    all_repuestos = repuestosEntity(collection_repuestos.find())
    return all_repuestos


# Crear Un Repuesto Con El Metodo POST
@repuesto.post("/repuesto", response_model=Repuesto)
async def create_repuesto(repuesto: Repuesto):
    new_repuesto = dict(repuesto)
    del new_repuesto["id"]

    id = collection_repuestos.insert_one(new_repuesto).inserted_id
    respuesto = repuestoEntity(collection_repuestos.find_one({"_id": ObjectId(id)}))
    return respuesto


# Obteniendo Un Solo Repuesto
@repuesto.get("/repuesto/{id}", response_model=Repuesto)
async def find_respuesto(id: str):
    one_repuesto = repuestoEntity(collection_repuestos.find_one({"_id": ObjectId(id)}))
    return one_repuesto

