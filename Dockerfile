FROM apache/airflow:2.8.1

# Instalar Selenium y otras librerías necesarias
RUN pip install --no-cache-dir selenium==4.23.1
