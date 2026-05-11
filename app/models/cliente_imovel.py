from sqlalchemy import Column, Integer, ForeignKey, String
from app.database.database import Base

class ClienteImovel(Base):
    __tablename__ = "cliente_imovel"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    data_interesse = Column(String)