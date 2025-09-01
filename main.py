from fastapi import FastAPI
from starlette.responses import Response

app = FastAPI()


@app.get("/ping")
async def root():
    return (Response('pong', status_code=200))
