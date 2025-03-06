from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from app.models.models import Table, MenuItem
import os


DB_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user1:123@localhost:3306/restaurant")
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Inserir mesas se não existirem
for i in range(1, 6):
    if not session.query(exists().where(Table.id == i)).scalar():
        session.add(Table(id=i, status="aberta"))

# Inserir itens no menu se não existirem
menu_items = [
    {"name": "Hambúrguer Clássico", "price": 2990},
    {"name": "Pizza Média", "price": 4590},
    {"name": "Salada Caesar", "price": 2490},
    {"name": "Refrigerante Lata", "price": 690},
    {"name": "Sobremesa Brownie", "price": 1990},
    {"name": "Suco de Laranja Natural", "price": 800},
    {"name": "Churrasco Misto", "price": 1990},
]

for item in menu_items:
    exists = session.query(MenuItem).filter_by(name=item["name"]).first()
    if not exists:
        session.add(MenuItem(**item))

session.commit()
session.close()

print("Banco de dados atualizado sem duplicações!")
