from fastapi import FastAPI
from app.modules.empleats.router import router as empleats_router
from app.modules.events.router import router as events_router
from app.modules.vendes.router import router as vendes_router
from app.modules.calendari.router import router as calendari_router
from app.modules.compres.router import router as compres_router
from app.modules.costos.router import router as costos_router
from app.modules.punts_de_venda.router import router as punts_de_venda_router
from app.modules.planificacio.router import router as planificacio_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(empleats_router, prefix="/api/empleats", tags=["Empleats"])
app.include_router(events_router, prefix="/api/events", tags=["Events"])
app.include_router(vendes_router, prefix="/api/vendes", tags=["Vendes"])
app.include_router(calendari_router, prefix="/api/calendari", tags=["Calendari"])
app.include_router(compres_router, prefix="/api/compres", tags=["Compres"])
app.include_router(costos_router, prefix="/api/costos", tags=["Costos"])
app.include_router(punts_de_venda_router, prefix="/api/punts_de_venda", tags=["Punts de Venda"])
app.include_router(planificacio_router, prefix="/api/planificacio", tags=["Planificació"])

@app.get("/")
def read_root():
    return {"message": "Institut TIC de Barcelona"}
