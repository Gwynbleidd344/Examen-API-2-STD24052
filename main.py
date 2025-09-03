from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, json
from starlette.responses import Response, JSONResponse

app = FastAPI()

class phonesModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: object = {
        "ram_memory": int,
        "rom_memory": int
    }

phone_list: List[phonesModel] = []

def serialized_phone_list():
    phone_converted = []
    for phone in phone_list:
        phone_converted.append(phone.model_dump())
    return phone_converted

@app.get("/health")
async def root():
    return (Response('Ok',status_code=200))

@app.post("/phones")
async def phone(newPhone: List[phonesModel]):
    phone_list.extend(newPhone)
    return JSONResponse(content={"phones": phone_list}, status_code=201)

@app.get("/phones")
async def phones():
    return JSONResponse(serialized_phone_list(), status_code=200)