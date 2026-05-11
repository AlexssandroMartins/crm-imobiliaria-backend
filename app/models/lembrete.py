from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Lembrete(Base):
    __tablename__ = "lembretes"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    data_retorno = Column(String)
    observacao = Column(String)