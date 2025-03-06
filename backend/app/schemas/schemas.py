from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Definição da estrutura base para uma mesa
class TableBase(BaseModel):
    status: str

# Modelo para criação de uma mesa (herda de TableBase)
class TableCreate(TableBase):
    pass 

# Resposta para uma mesa, incluindo o ID
class TableResponse(TableBase):
    id: int
    class Config:
         from_attributes = True  # Substituir orm_mode  

# Estrutura base para um item do menu
class MenuItemBase(BaseModel):
    name: str
    price: int  # Preço armazenado em centavos para evitar problemas com ponto flutuante

# Modelo para criação de um item do menu (herda de MenuItemBase)
class MenuItemCreate(MenuItemBase):
    pass

# Resposta para um item do menu, incluindo o ID
class MenuItemResponse(MenuItemBase):
    id: int
    class Config:
         from_attributes = True  # Substituir orm_mode

# Definição da estrutura base para um item de pedido
class OrderItemBase(BaseModel):
    menu_item_id: int  # Referência ao item do menu
    quantity: int      # Quantidade solicitada

# Modelo para criação de um item de pedido (herda de OrderItemBase)
class OrderItemCreate(OrderItemBase):
    pass

# Resposta para um item de pedido, incluindo o ID
class OrderItemResponse(OrderItemBase):
    id: int
    class Config:
         from_attributes = True  # Substituir orm_mode

# Definição da estrutura base para um pedido
class OrderBase(BaseModel):
    table_id: int  # Referência à mesa do pedido
    created_at: Optional[datetime] = None  # Data de criação opcional

# Modelo para criação de um pedido, agora incluindo itens
class OrderCreate(BaseModel):
    table_id: int  # Referência à mesa do pedido
    items: List[OrderItemCreate]  # Lista de itens no pedido

# Modelo de resposta para um pedido, incluindo ID e lista de itens
class OrderResponse(OrderBase):
    id: int
    total_price: int  # Total do pedido em centavos
    items: List[OrderItemResponse] = []  # Lista de itens no pedido
    class Config:
         from_attributes = True  # Substituir orm_mode
