# 🪙 Crypto ETL Pipeline

Pipeline ETL que extrae precios de las top 10 criptomonedas desde la API pública de CoinGecko, los transforma con Pandas, los almacena en PostgreSQL y los visualiza en un dashboard interactivo con Streamlit. Todo dockerizado.

## 🏗️ Arquitectura

```
CoinGecko API → Python (Extract) → Pandas (Transform) → PostgreSQL (Load) → Streamlit (Dashboard)
```

## 🛠️ Stack

- Python 3.11
- Pandas
- PostgreSQL 16
- SQLAlchemy
- Streamlit
- Docker & Docker Compose

## ✨ Features

- **Extract**: obtención automática de precios de las top 10 criptomonedas.
- **Transform**: limpieza, cálculo de volatilidad 24h y timestamp de ingesta.
- **Load**: carga en PostgreSQL con reemplazo automático (siempre datos frescos).
- **Dashboard**: visualización interactiva con métricas, gráficos y tabla.
- **Todo dockerizado**: se levanta con un solo comando.

## 🚀 Cómo ejecutarlo

1. Clona el repo:

   ```bash
   git clone https://github.com/tu-usuario/crypto-etl-pipeline.git
   cd crypto-etl-pipeline
   ```

2. Copia las variables de entorno:

   ```bash
   cp .env.example .env
   ```

3. Levanta los servicios (base de datos, pipeline y dashboard):

   ```bash
   docker compose up --build
   ```

4. Abre el dashboard en el navegador:

   ```
   http://localhost:8501
   ```

5. Verifica los datos en PostgreSQL:

   ```bash
   docker exec -it crypto_db psql -U crypto_user -d crypto_db -c "SELECT * FROM crypto_prices;"
   ```

## 📊 Dashboard

El dashboard incluye:

- **Métricas principales**: cantidad de criptomonedas, precio máximo y volatilidad promedio.
- **Gráfico de precios**: comparación visual de precios por criptomoneda.
- **Gráfico de volatilidad**: variación de las últimas 24 horas.
- **Tabla completa**: todos los datos extraídos y transformados.

## 📊 Transformaciones aplicadas

- Selección de columnas relevantes
- Cálculo de volatilidad 24h: `(high - low) / low * 100`
- Timestamp de ingesta en UTC
- Eliminación de registros sin precio

## 📁 Estructura del proyecto

```
crypto-etl-pipeline/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
└── src/
    ├── __init__.py
    ├── extract.py
    ├── transform.py
    ├── load.py
    ├── main.py
    └── dashboard.py
```

## 🔮 Mejoras futuras

- Orquestación con Airflow
- Tests con pytest
- Alertas por Telegram cuando la volatilidad supere X%
- Historial de precios (no solo el último estado)
- Deploy del dashboard en Streamlit Cloud

## 👤 Autor

Tu Nombre — Elsy Molina — www.linkedin.com/in/elsymolina — https://github.com/elsym18