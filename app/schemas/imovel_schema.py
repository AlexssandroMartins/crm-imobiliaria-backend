from pydantic import BaseModel
from typing import List

class ImovelCreate(BaseModel):
    descricao: str
    tipo: str
    status: str

class ImovelUpdate(BaseModel):
    descricao: str
    tipo: str
    status: str

class ImovelResponse(BaseModel):
    id: int
    descricao: str
    tipo: str
    status: str

    class Config:
        from_attributes = True
        
class ImovelListResponse(BaseModel):
    status: str
    dados: List[ImovelResponse]