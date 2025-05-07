def punt_schema(punt) -> dict:
    return {
        "Id_Punt": punt.Id_Punt,
        "Nom_Punt": punt.Nom_Punt,
        "Producte": punt.Producte,
        "Quantitat": punt.Quantitat,
        "Preu_Total": punt.Preu_Total,
        "Metode_Pagament": punt.Metode_Pagament,
        "Tiquet_Email": punt.Tiquet_Email,
        "Data_Venda": punt.Data_Venda
    }

def punts_schema(punts) -> list[dict]:
    return [punt_schema(p) for p in punts]
