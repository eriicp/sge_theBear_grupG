def compra_schema(compra) -> dict:
    return {
        "Id_Compra": compra.Id_Compra,
        "Data_Compra": compra.Data_Compra,
        "Proveidor": compra.Proveidor,
        "Producte_Compra": compra.Producte_Compra,
        "Quantitat": compra.Quantitat,
        "Preu_Unitari": compra.Preu_Unitari,
        "Total": compra.Total,
        "Estat_Comanda": compra.Estat_Comanda
    }

def compres_schema(compres) -> list[dict]:
    return [compra_schema(c) for c in compres]
