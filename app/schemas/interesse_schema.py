from pydantic import BaseModel
from typing import List

class InteresseCreate(BaseModel):
    cliente_id: int
    imovel_id: int
    data_interesse: str

class InteresseResponse(BaseModel):
    id: int
    cliente_id: int
    imovel_id: int
    data_interesse: str

    class Config:
        from_attributes = True

class InteresseListResponse(BaseModel):
    status: str
    dados: List[InteresseResponse]