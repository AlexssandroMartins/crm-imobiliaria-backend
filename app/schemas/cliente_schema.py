from pydantic import BaseModel

class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    interesse: str
    status: str

class ClienteUpdate(BaseModel):
    nome: str
    telefone: str
    interesse: str
    status: str