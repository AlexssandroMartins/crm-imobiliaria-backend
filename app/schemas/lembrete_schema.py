from pydantic import BaseModel
from typing import List
from pydantic import BaseModel

class LembreteCreate(BaseModel):
    cliente_id: int
    data_retorno: str
    observacao: str

class LembreteResponse(BaseModel):
    id: int
    cliente_id: int
    data_retorno: str
    observacao: str

    class Config:
        from_attributes = True

class LembreteListResponse(BaseModel):
    status: str
    dados: List[LembreteResponse]