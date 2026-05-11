from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.cliente import Cliente
from app.schemas.cliente_schema import ClienteCreate, ClienteUpdate

router = APIRouter()

@router.post("/clientes")
def criar_cliente(dados: ClienteCreate):
    db: Session = SessionLocal()

    novo_cliente = Cliente(
        nome=dados.nome,
        telefone=dados.telefone,
        interesse=dados.interesse,
        status=dados.status
    )

    db.add(novo_cliente)
    db.commit()
    db.refresh(novo_cliente)

    return {"mensagem": "Cliente criado com sucesso", "cliente": novo_cliente}

@router.get("/clientes")
def listar_clientes():
    db: Session = SessionLocal()
    clientes = db.query(Cliente).all()

    return {
        "status": "sucesso",
        "dados": clientes
    }

@router.get("/clientes/buscar")
def buscar_cliente(nome: str):
    db: Session = SessionLocal()
    clientes = db.query(Cliente).filter(Cliente.nome.ilike(f"{nome}%")).all()

    return {
        "status": "sucesso",
        "dados": clientes
    }

@router.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    db: Session = SessionLocal()

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        return {"erro": "Cliente não encontrado"}

    db.delete(cliente)
    db.commit()

    return {"mensagem": "Cliente deletado com sucesso"}

@router.put("/clientes/{cliente_id}")
def atualizar_cliente(cliente_id: int, dados: ClienteUpdate):
    db: Session = SessionLocal()

    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        return {"erro": "Cliente não encontrado"}

    cliente.nome = dados.nome
    cliente.telefone = dados.telefone
    cliente.interesse = dados.interesse
    cliente.status = dados.status

    db.commit()
    db.refresh(cliente)

    return {"mensagem": "Cliente atualizado com sucesso", "cliente": cliente}