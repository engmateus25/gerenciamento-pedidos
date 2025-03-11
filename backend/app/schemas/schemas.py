from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class TableBase(BaseModel):
    status: str


class TableCreate(TableBase):
    pass 


class TableResponse(TableBase):
    id: int
    class Config:
         from_attributes = True   


class MenuItemBase(BaseModel):
    name: str
    price: int  


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemResponse(MenuItemBase):
    id: int
    class Config:
         from_attributes = True 


class OrderItemBase(BaseModel):
    menu_item_id: int  
    quantity: int      


class OrderItemCreate(OrderItemBase):
    pass


class OrderItemResponse(OrderItemBase):
    id: int
    class Config:
         from_attributes = True 


class OrderBase(BaseModel):
    table_id: int  
    created_at: Optional[datetime] = None  


class OrderCreate(BaseModel):
    table_id: int  
    items: List[OrderItemCreate]  


class OrderResponse(OrderBase):
    id: int
    total_price: int  
    items: List[OrderItemResponse] = []  
    class Config:
         from_attributes = True  
