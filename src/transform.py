import pandas as pd
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

COLUMNS = [
    "id", "symbol", "name", "current_price", "market_cap",
    "market_cap_rank", "total_volume", "high_24h", "low_24h",
    "price_change_percentage_24h",
]


def transform_crypto_data(raw_data: list[dict]) -> pd.DataFrame:
    """Limpia y enriquece los datos crudos."""
    logger.info("Transformando datos...")
    df = pd.DataFrame(raw_data)

    # Seleccionar columnas relevantes
    df = df[[c for c in COLUMNS if c in df.columns]].copy()

    # Renombrar
    df = df.rename(columns={
        "high_24h": "high_24h_usd",
        "low_24h": "low_24h_usd",
    })

    # Tipos
    df["market_cap_rank"] = df["market_cap_rank"].astype("Int64")
    df["price_change_percentage_24h"] = df["price_change_percentage_24h"].round(2)

    # Métrica derivada: volatilidad diaria aproximada
    df["volatility_24h"] = ((df["high_24h_usd"] - df["low_24h_usd"]) / df["low_24h_usd"] * 100).round(2)

    # Timestamp de ingesta
    df["extracted_at"] = datetime.now(timezone.utc)

    # Eliminar nulos en price
    df = df.dropna(subset=["current_price"])

    logger.info(f"DataFrame final: {df.shape[0]} filas, {df.shape[1]} columnas.")
    return df