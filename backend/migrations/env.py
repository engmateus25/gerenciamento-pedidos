from logging.config import fileConfig
from sqlalchemy import engine_from_config  # Cria um engine com base nas configurações
from sqlalchemy import pool  # define um pool de conexões com o banco de dados
from alembic import context  # Importa o contexto do Alembic para gerenciar as migrações
from app.models.models import Table, MenuItem, Order, OrderItem 
from app.db import Base  # Importa a base do arquivo db.py



target_metadata = Base.metadata  # Define os metadados das tabelas que serão monitoradas para migração
config = context.config   # pega a configuração do Alembic a partir do arquivo alembic.ini

# Configura o logging, se um arquivo de configuração estiver definido
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    """Executa as migrações no modo offline.

    O modo offline não requer um engine do SQLAlchemy,
    apenas a URL de conexão com o banco de dados.
    Os comandos são convertidos em scripts SQL.
    """
    url = config.get_main_option("sqlalchemy.url")  # obtém a URL do banco de dados do alembic.ini
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,  # Usa valores literais em vez de parâmetros
        dialect_opts={"paramstyle": "named"},  # Define o estilo dos parâmetros da query
    )

    with context.begin_transaction():  # Inicia uma transação
        context.run_migrations()  # executa as migrações



def run_migrations_online() -> None:
    """Executa as migrações no modo online.

    O modo online cria um engine e se conecta ao banco de dados,
    permitindo que as migrações sejam aplicadas diretamente.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),  # Obtém as configurações do banco
        prefix="sqlalchemy.",  # prefixo para os parâmetros do SQLAlchemy no alembic.ini
        poolclass=pool.NullPool,  # Desativa o pooling de conexões
    )

    with connectable.connect() as connection:  # Abre uma conexão com o banco de dados
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():  # Inicia uma transação
            context.run_migrations()  # Executa as migrações


# Determina se a execução será no modo offline ou online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
