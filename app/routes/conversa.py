from fastapi import APIRouter, Depends
from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.conversa import Conversa
from app.schemas.conversa_schema import ConversaCreate, ConversaResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/conversas", response_model=ConversaResponse)
def criar_conversa(dados: ConversaCreate):
    db: Session = SessionLocal()

    nova_conversa = Conversa(
        cliente_id=dados.cliente_id,
        mensagem=dados.mensagem
    )

    db.add(nova_conversa)
    db.commit()
    db.refresh(nova_conversa)

    return nova_conversa

@router.get("/conversas")
def listar_conversas(db: Session = Depends(get_db)):
    conversas = db.query(Conversa).all()
    
    return {
    "status": "sucesso",
    "dados": conversas
}

@router.get("/clientes/{cliente_id}/conversas", response_model=list[ConversaResponse])
def listar_conversas_por_cliente(cliente_id: int, db: Session = Depends(get_db)):
    conversas = db.query(Conversa).filter(Conversa.cliente_id == cliente_id).all()
    return conversas