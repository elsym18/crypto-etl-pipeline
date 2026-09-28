import logging
from src.extract import extract_crypto_data
from src.transform import transform_crypto_data
from src.load import load_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger(__name__)


def run_pipeline():
    logger.info("🚀 Iniciando pipeline ETL de criptomonedas")
    raw = extract_crypto_data(vs_currency="usd", top_n=10)
    df = transform_crypto_data(raw)
    load_data(df)
    logger.info("✅ Pipeline finalizado con éxito")


if __name__ == "__main__":
    run_pipeline()