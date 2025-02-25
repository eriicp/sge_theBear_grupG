from typing import List
from fastapi import FastAPI
from services import read

app = FastAP1()

@app.get("/root", respnse_model=list[dict])
async def read_root():
    result = read.registre()
    return result