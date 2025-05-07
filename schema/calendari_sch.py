def reunio_schema(reunio) -> dict:
    return {
        "Id_Reunio": reunio.Id_Reunio,
        "Nom_Reunio": reunio.Nom_Reunio,
        "Data_Reunio": reunio.Data_Reunio,
        "Hora_Inici": reunio.Hora_Inici,
        "Hora_Fi": reunio.Hora_Fi,
        "Ubicacio_Reunio": reunio.Ubicacio_Reunio,
        "Etiquetes": reunio.Etiquetes,
        "Recurrencia": reunio.Recurrencia
    }

def reunions_schema(reunions) -> list[dict]:
    return [reunio_schema(r) for r in reunions]
