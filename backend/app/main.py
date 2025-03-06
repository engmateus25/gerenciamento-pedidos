from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Importa o middleware de CORS
from app.db import engine
from app.models import models
from app.routes import tables, menu_items, orders

# Cria as tabelas no banco de dados caso ainda não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI()   # Inicializa a aplicação FastAPI

# Adiciona o middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos os domínios ou substitua por uma lista específica de URLs
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

# Inclui os roteadores das rotas
app.include_router(tables.router)
app.include_router(menu_items.router)
app.include_router(orders.router)

# Rota raiz para verificar se a API está funcionando
@app.get("/")
def root():
    return {"message": "API funcionando gente!"}
