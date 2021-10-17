from bson import ObjectId
from fastapi import APIRouter, HTTPException

from config.database import collection_repuestos
from models.repuesto_model import Repuesto
from schemas.repuestos_schemas import repuestoEntity, repuestosEntity

repuesto = APIRouter()


# Mostrando Todos los Repuestos
@repuesto.get("/repuestos", response_model = list[Repuesto])
async def find_all_repuestos():
	all_repuestos = repuestosEntity(collection_repuestos.find())
	return all_repuestos


# Crear Un Repuesto Con El Método POST
@repuesto.post("/repuesto", response_model = Repuesto)
async def create_repuesto(repuesto: Repuesto):
	new_repuesto = dict(repuesto)
	del new_repuesto["id"]

	id = collection_repuestos.insert_one(new_repuesto).inserted_id
	respuesto = repuestoEntity(collection_repuestos.find_one({"_id": ObjectId(id)}))
	return respuesto


# Obteniendo Un Solo Repuesto Por id
@repuesto.get("/repuestos/{id}", response_description = "Consiga un solo repuesto", response_model = Repuesto, )
async def find_respuesto(id: str):
	if (one_repuesto := repuestoEntity(collection_repuestos.find_one({"_id": ObjectId(id)}))) is not None:
		return one_repuesto
	raise HTTPException(status_code = 404, detail = f"Repuesto {id} not found")


# Obteniendo Un Solo Repuesto Por Referencia
@repuesto.get("/repuesto/{referencia}", response_description = "Consiga un solo repuesto por Referencia", response_model = Repuesto)
async def find_repuesto_by_referencia(referencia: str):
	if (one_repuesto_referencia := repuestoEntity(collection_repuestos.find_one({"referencia": referencia}))) is not None:
		return one_repuesto_referencia
	raise HTTPException(status_code = 404, detail = f"El repuesto con esa referencia{referencia} no se encontró", )
