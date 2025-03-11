from logging.config import fileConfig
from sqlalchemy import create_engine, pool  
from alembic import context
from app.models.models import Table, MenuItem, Order, OrderItem
from app.db import Base, DB_URL  



config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa as migrações no modo offline."""
    context.configure(
        url=DB_URL, 
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações no modo online."""
    connectable = create_engine(DB_URL, poolclass=pool.NullPool) 

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
