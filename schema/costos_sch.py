def cost_schema(cost) -> dict:
    return {
        "Id_Cost": cost.Id_Cost,
        "Descripcio": cost.Descripcio,
        "Categoria": cost.Categoria,
        "Quantitat": cost.Quantitat,
        "Data_Cost": cost.Data_Cost,
        "Pagat_Per": cost.Pagat_Per
    }

def costos_schema(costos) -> list[dict]:
    return [cost_schema(c) for c in costos]
