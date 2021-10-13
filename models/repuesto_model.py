from pydantic import BaseModel
from typing import Optional


class Repuesto(BaseModel):
    id: Optional[str]
    referencia: str
    descripcion: str
    unidad_de_venta: int
    precio_antes_iva: int
    precio_con_iva: int
