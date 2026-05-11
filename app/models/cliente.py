from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    interesse = Column(String)
    status = Column(String)