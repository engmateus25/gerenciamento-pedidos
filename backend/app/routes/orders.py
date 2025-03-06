from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import models
from app.schemas import schemas
from datetime import datetime, date



router = APIRouter(prefix="/orders", tags=["Orders"])


def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()


# Rota para criar um novo pedido e calcular o preço
@router.post("/", response_model=schemas.OrderResponse)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    # Criar o pedido
    db_order = models.Order(
        table_id=order.table_id,
        total_price=0,  # Inicialmente zero, será atualizado depois
        created_at=datetime.utcnow()
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    total_price = 0  # Calcular o preço total do pedido
    order_items = []

    for item in order.items:
        menu_item = db.query(models.MenuItem).filter(models.MenuItem.id == item.menu_item_id).first()
        if not menu_item:
            raise HTTPException(status_code=404, detail=f"Item do menu com ID {item.menu_item_id} não encontrado")

        item_total = menu_item.price * item.quantity
        total_price += item_total

        order_item = models.OrderItem(
            order_id=db_order.id,
            menu_item_id=item.menu_item_id,
            quantity=item.quantity
        )
        order_items.append(order_item)
    
    db.add_all(order_items)  # Adiciona todos os itens do pedido ao banco
    db.commit()

    # Atualizar o total_price do pedido
    db_order.total_price = total_price
    db.commit()
    db.refresh(db_order)

    return db_order


# Rota para o resumo de pedidos (tem que ser colocada antes de outras rotas com parâmetros dinâmicos)
@router.get("/summary", response_model=dict)
def get_orders_summary(db: Session = Depends(get_db)):
    today = date.today()
    start_of_day = datetime.combine(today, datetime.min.time())  # 00:00:00
    end_of_day = datetime.combine(today, datetime.max.time())  # 23:59:59.999999

    total_orders = db.query(models.Order).filter(
        models.Order.created_at >= start_of_day,
        models.Order.created_at <= end_of_day
    ).count()

    return {"total_orders_today": total_orders}


# rota para obter todos os pedidos cadastrados
@router.get("/", response_model=list[schemas.OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all() 


# Busca um pedido pelo ID
@router.get("/{order_id}", response_model=schemas.OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# Atualiza os dados do pedido pelo ID
@router.put("/{order_id}", response_model=schemas.OrderResponse)
def update_order(order_id: int, updated_order: schemas.OrderCreate, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    order.table_id = updated_order.table_id
    order.total_price = updated_order.total_price

    db.commit()
    db.refresh(order)
    return order


# Deleta um pedido pelo ID
@router.delete("/{order_id}", response_model=dict)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    db.delete(order)
    db.commit()
    return {"message": "Order deleted successfully"}
