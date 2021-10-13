from fastapi import FastAPI
from routes.repuesto import repuesto

app = FastAPI(
    title='API-REST DE REPUESTOS CON FASTAPI Y MONGODB',
    description='Una simple REST-API de repuestos',
    version='0.0.1'
)


# Aquí LLamamos a la ruta de repuestos
app.include_router(repuesto, tags=['Lista de Repuestos'])
