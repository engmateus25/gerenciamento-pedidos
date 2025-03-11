from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db import Base
from datetime import datetime
from sqlalchemy import String



class Table(Base):
    __tablename__ = "tables"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String(50), default="aberta")

    orders = relationship("Order", back_populates="table", cascade="all, delete-orphan")


class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String(255), nullable=False, index=True)  
    price = Column(Integer)  


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)  
    table_id = Column(Integer, ForeignKey("tables.id"))  
    total_price = Column(Integer)  
    created_at = Column(DateTime, default=datetime.utcnow)  

    table = relationship("Table", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")  


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)  
    order_id = Column(Integer, ForeignKey("orders.id"))  
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))  
    quantity = Column(Integer)  

    order = relationship("Order", back_populates="items")  

