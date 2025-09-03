from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get("/health")
async def root():
    return (Response('Ok',status_code=200))
