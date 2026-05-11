from pydantic import BaseModel
from typing import Any

class ResponsePadrao(BaseModel):
    status: str
    dados: Any