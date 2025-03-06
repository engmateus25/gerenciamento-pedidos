from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from datetime import datetime
from sqlalchemy import String


# Modelo para representar uma mesa no restaurante
class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), default="aberta")

    # Relacionamento com pedidos, ativando delete em cascata
    orders = relationship("Order", back_populates="table", cascade="all, delete-orphan")


class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)  # ID único do item do menu
    name = Column(String(255), nullable=False, index=True)  # Nome do item
    price = Column(Integer)  # preço em centavos, ex: 100 = R$1,00


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  
    table_id = Column(Integer, ForeignKey("tables.id"))  
    total_price = Column(Integer)  
    created_at = Column(DateTime, default=datetime.utcnow)  

    table = relationship("Table", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")  # Adicionando relacionamento


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)  
    order_id = Column(Integer, ForeignKey("orders.id"))  
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))  
    quantity = Column(Integer)  

    order = relationship("Order", back_populates="items")  # Adicionando back_populates para garantir a ligação

