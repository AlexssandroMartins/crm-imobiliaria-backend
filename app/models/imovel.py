from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Imovel(Base):
    __tablename__ = "imoveis"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String)
    tipo = Column(String)  # casa, apartamento...
    status = Column(String)  # disponível, vendido, alugado