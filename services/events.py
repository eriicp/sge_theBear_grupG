from sqlmodel import Session
from models.events import Event

def add_event(Nom_Event, Data_Event, Hora_Event, Ubicacio_Event, Organitzador_Event, Estat_Event, Entrades_Disponibles, Privat, db: Session):
    event = Event(
        Nom_Event=Nom_Event,
        Data_Event=Data_Event,
        Hora_Event=Hora_Event,
        Ubicacio_Event=Ubicacio_Event,
        Organitzador_Event=Organitzador_Event,
        Estat_Event=Estat_Event,
        Entrades_Disponibles=Entrades_Disponibles,
        Privat=Privat
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"message": "Event creat correctament"}

def get_all_events(db: Session):
    return [e.dict() for e in db.query(Event).all()]

def get_event_by_id(id: int, db: Session):
    event = db.query(Event).filter(Event.Id_Event == id).first()
    return event.dict() if event else {}

def update_event(id, Nom_Event, Data_Event, Hora_Event, Ubicacio_Event, Organitzador_Event, Estat_Event, Entrades_Disponibles, Privat, db: Session):
    event = db.query(Event).filter(Event.Id_Event == id).first()
    if event is None:
        return {}
    if Nom_Event is not None: event.Nom_Event = Nom_Event
    if Data_Event is not None: event.Data_Event = Data_Event
    if Hora_Event is not None: event.Hora_Event = Hora_Event
    if Ubicacio_Event is not None: event.Ubicacio_Event = Ubicacio_Event
    if Organitzador_Event is not None: event.Organitzador_Event = Organitzador_Event
    if Estat_Event is not None: event.Estat_Event = Estat_Event
    if Entrades_Disponibles is not None: event.Entrades_Disponibles = Entrades_Disponibles
    if Privat is not None: event.Privat = Privat
    db.commit()
    db.refresh(event)
    return event.dict()

def delete_event(id: int, db: Session):
    event = db.query(Event).filter(Event.Id_Event == id).first()
    if event is None:
        return {}
    db.delete(event)
    db.commit()
    return {"message": "Event eliminat correctament"}
