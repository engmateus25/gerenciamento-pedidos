from sqlalchemy import create_engine   # para conectar ao banco de dados
from sqlalchemy.orm import sessionmaker, declarative_base # sessionmaker para gerenciar as sessões do banco e declarative_base para criar modelos ORM
import os  # para acessar variáveis de ambiente
from dotenv import load_dotenv  # para carregar variáveis do arquivo .env


load_dotenv()  # carrega as variáveis de ambiente do arquivo .env

# Montando a URL de conexão com o banco de dados, substituindo os place holders pelas variaveis de ambiente
DB_URL = f"mariadb+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"  

engine = create_engine(DB_URL)  # gerenciando a comunicação com o banco de dados

# criando uma fábrica de sessões do SQLAlchemy, permitindo interações com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  

Base = declarative_base()  # Cria uma classe base para os modelos ORM, tabelas do banco de dados


# Criar sessão do banco de dados para ser usada nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()