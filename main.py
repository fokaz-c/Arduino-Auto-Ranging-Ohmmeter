from typing import Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.serialConnection import serialConnection


app = FastAPI()

sc = serialConnection('COM3', 9600)
sc.open_connection()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"resistance": sc.read_data()}
