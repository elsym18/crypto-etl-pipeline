import requests
import logging

logger = logging.getLogger(__name__)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"


def extract_crypto_data(vs_currency: str = "usd", top_n: int = 10) -> list[dict]:
    """Extrae las top N criptomonedas desde CoinGecko."""
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
        "sparkline": "false",
    }
    logger.info(f"Extrayendo top {top_n} criptos en {vs_currency}...")
    response = requests.get(API_URL, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()
    logger.info(f"Se obtuvieron {len(data)} registros.")
    return data