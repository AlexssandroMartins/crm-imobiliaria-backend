from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Conversa(Base):
    __tablename__ = "conversas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    mensagem = Column(String)