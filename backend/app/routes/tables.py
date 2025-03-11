from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import models
from app.schemas import schemas



# Criando um roteador para gerenciar as rotas relacionadas a Tables
router = APIRouter(prefix="/tables", tags=["Tables"])


# obtendo a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db  # Garante que a sessão seja fechada corretamente após o uso
    finally:
        db.close()


# Rota para criar uma nova mesa
@router.post("/", response_model=schemas.TableResponse)
def create_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
    db_table = models.Table(status=table.status)  # Cria um novo objeto Table
    db.add(db_table)  # Adiciona ao banco de dados
    db.commit()  # salvando as mudanças
    db.refresh(db_table)  # Atualiza o objeto com os dados persistidos
    return db_table  # Retorna a mesa criada


# Rota para obter todas as mesas cadastradas
@router.get("/", response_model=list[schemas.TableResponse])
def get_tables(db: Session = Depends(get_db)):
    return db.query(models.Table).all()  # Retorna todas as mesas do banco


# Rota para obter uma mesa específica pelo ID
@router.get("/{table_id}", response_model=schemas.TableResponse)
def get_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")  # Retorna erro se não existir
    return table  # Retorna a mesa encontrada


# Fecha a conta de uma mesa pelo ID.
@router.post("/{table_id}/close", response_model=dict)
def close_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(models.Table).filter(models.Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail="Table not found")

    # Buscar os pedidos da mesa
    orders = db.query(models.Order).filter(models.Order.table_id == table_id).all()

    if not orders:
        return {"message": "Table closed. No orders found.", "total_price": 0}

    # Calcular o total da conta (soma do total_price de todos os pedidos)
    total_price = sum(order.total_price for order in orders)

    # Deletar todos os itens de pedidos associados aos pedidos da mesa
    for order in orders:
        db.query(models.OrderItem).filter(models.OrderItem.order_id == order.id).delete()

    # Excluir todos os pedidos vinculados à mesa
    db.query(models.Order).filter(models.Order.table_id == table_id).delete()
    
    # Atualizar status da mesa para "fechada"
    table.status = "fechada"

    db.commit()
    
    return {
        "message": "Table closed and orders deleted",
        "total_price": total_price
    }

