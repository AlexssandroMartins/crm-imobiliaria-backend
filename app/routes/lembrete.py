from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.lembrete import Lembrete
from app.schemas.lembrete_schema import LembreteCreate, LembreteResponse
from app.schemas.lembrete_schema import LembreteCreate, LembreteResponse, LembreteListResponse

router = APIRouter()

@router.post("/lembretes", response_model=LembreteResponse)
def criar_lembrete(dados: LembreteCreate):
    db: Session = SessionLocal()

    novo_lembrete = Lembrete(
        cliente_id=dados.cliente_id,
        data_retorno=dados.data_retorno,
        observacao=dados.observacao
    )

    db.add(novo_lembrete)
    db.commit()
    db.refresh(novo_lembrete)

    return novo_lembrete

@router.get("/lembretes", response_model=LembreteListResponse)
def listar_lembretes():
    db: Session = SessionLocal()
    lembretes = db.query(Lembrete).all()

    return {
    "status": "sucesso",
    "dados": lembretes
 }