from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import cliente as rota_cliente
from app.routes import conversa as rota_conversa
from app.routes import lembrete as rota_lembrete
from app.routes import imovel as rota_imovel
from app.routes import cliente_imovel as rota_cliente_imovel
from app.routes import interesse as rota_interesse

from app.models.cliente import Cliente
from app.models.conversa import Conversa
from app.models.lembrete import Lembrete
from app.models.imovel import Imovel
from app.models.cliente_imovel import ClienteImovel
from app.database.database import Base, engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(rota_cliente.router)
app.include_router(rota_conversa.router)
app.include_router(rota_lembrete.router)
app.include_router(rota_imovel.router)
app.include_router(rota_interesse.router)
app.include_router(rota_cliente_imovel.router)

@app.get("/")
def home():
    return {"mensagem": "CRM Imobiliário rodando 🚀"}