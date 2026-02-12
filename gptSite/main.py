from contextlib import asynccontextmanager
from ipaddress import ip_address

from fastapi import FastAPI, Body,Request
from fastapi.middleware.cors import CORSMiddleware
from config import Config
from Gpt_Client import GPTClient
from db import Base, add_request_data,engine,get_user_request

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("Все таблицы созданы")
    yield

app=FastAPI(lifespan=lifespan)

# Настройка CORS для работы с фронтендом на localhost:5500
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/requests")
def get_my_requests(request:Request):
    user_ip_adress = request.client.host
    print(f"{user_ip_adress}")
    user_requests=get_user_request(ip_address=user_ip_adress)
    return user_requests

@app.post("/requests")
def send_prompt(
    request:Request,
    prompt: str = Body(embed=True),
):
    user_ip_address = request.client.host
    answer = GPTClient().get_answer_from_gpt(prompt)
    add_request_data(
        ip_address=user_ip_address,
        prompt=prompt,
        response=answer,

    )
    return {"answer": answer}