from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.imovel import Imovel
from app.schemas.imovel_schema import ImovelCreate, ImovelResponse
from app.schemas.imovel_schema import ImovelCreate, ImovelResponse, ImovelListResponse

router = APIRouter()

@router.post("/imoveis", response_model=ImovelResponse)
def criar_imovel(dados: ImovelCreate):
    db: Session = SessionLocal()

    novo_imovel = Imovel(
        descricao=dados.descricao,
        tipo=dados.tipo,
        status=dados.status
    )

    db.add(novo_imovel)
    db.commit()
    db.refresh(novo_imovel)

    return novo_imovel

@router.get("/imoveis", response_model=ImovelListResponse)
def listar_imoveis():
    db: Session = SessionLocal()
    imoveis = db.query(Imovel).all()

    return {
        "status": "sucesso",
        "dados": imoveis
    }