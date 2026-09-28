import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Crypto Dashboard", page_icon="🪙", layout="wide")

st.title("🪙 Crypto Dashboard")
st.markdown("Datos en tiempo real de las top 10 criptomonedas desde CoinGecko.")

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = os.getenv("POSTGRES_HOST", "db")
port = os.getenv("POSTGRES_PORT", "5432")
db = os.getenv("POSTGRES_DB")

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")

@st.cache_data(ttl=60)
def load_data():
    query = "SELECT * FROM crypto_prices ORDER BY market_cap_rank"
    return pd.read_sql(query, engine)

try:
    df = load_data()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Criptomonedas", len(df))
    with col2:
        st.metric("Precio máx (USD)", f"${df['current_price'].max():,.0f}")
    with col3:
        st.metric("Volatilidad prom.", f"{df['volatility_24h'].mean():.2f}%")

    st.subheader("📊 Precios por criptomoneda")
    st.bar_chart(df.set_index("name")["current_price"])

    st.subheader("📈 Volatilidad 24h")
    st.bar_chart(df.set_index("name")["volatility_24h"])

    st.subheader("📋 Datos completos")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Error al cargar datos: {e}")
    st.info("Asegurate de que el pipeline haya corrido al menos una vez.")