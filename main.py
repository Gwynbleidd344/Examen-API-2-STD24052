from typing import List

from fastapi import FastAPI
from pydantic import BaseModel, json
from starlette.responses import Response, JSONResponse

app = FastAPI()

class CharacteristicsModel(BaseModel):
    ram_memory: int
    rom_memory: int

class phonesModel(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: CharacteristicsModel

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
    return JSONResponse(content={"phones": serialized_phone_list()}, status_code=201)

@app.get("/phones")
async def phones():
    return JSONResponse(serialized_phone_list(), status_code=200)

@app.get("/phones/{id}")
async def get_phone_by_id(id: str):
    for phone_data in serialized_phone_list():
        if phone_data["identifier"] == id:
            return JSONResponse(content={"phone": phone_data}, status_code=200)
    return Response("Phone not found", status_code=404)

@app.put("/phones/{id}/characteristics")
async def update_phone_characteristics(id: str, characteristics: CharacteristicsModel):
    for phone in phone_list:
        if phone.identifier == id:
            phone.characteristics = characteristics
            return JSONResponse(content={"phone": phone.model_dump()}, status_code=200)
    return Response("Phone not found", status_code=404)
