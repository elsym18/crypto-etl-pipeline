import os
import logging
import pandas as pd
from sqlalchemy import create_engine, text

logger = logging.getLogger(__name__)


def get_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB")
    url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
    return create_engine(url)


def load_data(df: pd.DataFrame, table_name: str = "crypto_prices") -> None:
    """Carga el DataFrame en PostgreSQL, creando la tabla si no existe."""
    logger.info(f"Cargando {len(df)} filas en '{table_name}'...")
    engine = get_engine()

    with engine.begin() as conn:
        conn.execute(text(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id TEXT,
                symbol TEXT,
                name TEXT,
                current_price NUMERIC,
                market_cap NUMERIC,
                market_cap_rank INTEGER,
                total_volume NUMERIC,
                high_24h_usd NUMERIC,
                low_24h_usd NUMERIC,
                price_change_percentage_24h NUMERIC,
                volatility_24h NUMERIC,
                extracted_at TIMESTAMPTZ
            );
        """))

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    logger.info("Carga completada ✅")