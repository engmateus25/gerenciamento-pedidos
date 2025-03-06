from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import models
from app.schemas import schemas



# gerenciando as rotas relacionadas aos itens do menu
router = APIRouter(prefix="/menu-items", tags=["Menu Items"])


# Dependência para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()


# Rota para criar um novo item do menu
@router.post("/", response_model=schemas.MenuItemResponse)
def create_menu_item(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    db_item = models.MenuItem(**item.dict())  # Cria um novo objeto MenuItem com os dados recebidos
    db.add(db_item)  # Adiciona ao banco de dados
    db.commit()  # salvando as mudanças
    db.refresh(db_item)  # Atualiza o objeto com os dados persistidos
    return db_item  


# para obter todos os itens do menu cadastrados
@router.get("/", response_model=list[schemas.MenuItemResponse])
def get_menu_items(db: Session = Depends(get_db)):
    return db.query(models.MenuItem).all()  # Retorna todos os itens do menu do banco
