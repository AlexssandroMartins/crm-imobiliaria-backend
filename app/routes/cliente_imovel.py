from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.cliente_imovel import ClienteImovel
from app.schemas.interesse_schema import InteresseCreate, InteresseResponse

router = APIRouter()

@router.post("/interesses", response_model=InteresseResponse)
def criar_interesse(dados: InteresseCreate):
    db: Session = SessionLocal()

    novo_interesse = ClienteImovel(
        cliente_id=dados.cliente_id,
        imovel_id=dados.imovel_id,
        data_interesse=dados.data_interesse
    )

    db.add(novo_interesse)
    db.commit()
    db.refresh(novo_interesse)

    return novo_interesse

@router.get("/interesses", response_model=list[InteresseResponse])
def listar_interesses():
    db: Session = SessionLocal()
    interesses = db.query(ClienteImovel).all()
    return interesses