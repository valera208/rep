from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine  # синхронный движок для Alembic
from sqlalchemy import MetaData
from alembic import context

# импорт моделей
from database import Base  # твой Base
from models.users import Users
from models.posts import Posts

from models.profiles import Profiles
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
fileConfig(config.config_file_name)

# metadata всех моделей
target_metadata = Base.metadata

# Синхронный URL для Alembic
# Если твой async URL был: postgresql+asyncpg://user:pass@localhost/db
# Синхронный будет: postgresql://user:pass@localhost/db
SYNC_SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:54545/postgresdb"

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = SYNC_SQLALCHEMY_DATABASE_URL
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    # используем синхронный движок для Alembic
    connectable = create_engine(
        SYNC_SQLALCHEMY_DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
