def repuestoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "referencia": item["referencia"],
        "descripcion": item["descripcion"],
        "unidad_de_venta": item["unidad_de_venta"],
        "precio_antes_iva": item["precio_antes_iva"],
        "precio_con_iva": item["precio_con_iva"],
    }


def repuestosEntity(entity) -> list:
    return [repuestoEntity(item) for item in entity]
