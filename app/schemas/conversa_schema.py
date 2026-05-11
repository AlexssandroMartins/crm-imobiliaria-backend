from pydantic import BaseModel

class ConversaCreate(BaseModel):
    cliente_id: int
    mensagem: str

class ConversaResponse(BaseModel):
    id: int
    cliente_id: int
    mensagem: str

    class Config:
        from_attributes = True