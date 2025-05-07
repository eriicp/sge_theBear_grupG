def event_schema(event) -> dict:
    return {
        "Id_Event": event.Id_Event,
        "Nom_Event": event.Nom_Event,
        "Data_Event": event.Data_Event,
        "Hora_Event": event.Hora_Event,
        "Ubicacio_Event": event.Ubicacio_Event,
        "Organitzador_Event": event.Organitzador_Event,
        "Estat_Event": event.Estat_Event,
        "Entrades_Disponibles": event.Entrades_Disponibles,
        "Privat": event.Privat
    }

def events_schema(events) -> list[dict]:
    return [event_schema(e) for e in events]
