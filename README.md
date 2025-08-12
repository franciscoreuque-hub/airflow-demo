# Airflow + Selenium Web Scraping Demo

[![Airflow](https://img.shields.io/badge/Airflow-2.8.1-blue)](https://airflow.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3.9-orange)](https://docs.docker.com/compose/compose-file/compose-versioning/)

---

> *This repo was thought for demostrate how to get running a containerized Apache Airflow DAG that uses Selenium to scrape product data from a dynamic e-commerce site.*

---

## How to run (local)

1. **Create the output directory and give correct permissions:**
    ```bash
    mkdir -p dags/output
    # Optional: change owner to match AIRFLOW_UID if needed
    # sudo chown -R 50000:0 dags/output
    ```

2. **Provide secret values in a `.env` file (example):**
    ```ini
    AIRFLOW__CORE__FERNET_KEY=replace_with_your_fernet_key
    AIRFLOW__WEBSERVER__SECRET_KEY=replace_with_your_secret
    AIRFLOW_UID=50000
    ```

3. **Build & start:**
    ```bash
    docker-compose up --build -d
    ```

4. **Initialize Airflow (creates DB + admin user):**
    ```bash
    docker-compose run airflow-init
    ```

5. **Open Airflow UI:**  
   Go to [http://localhost:8080](http://localhost:8080) (credentials: `admin/admin`)  
   Trigger `DAG coto_verificar_productos` manually from the UI or via CLI.

6. **Inspect artifacts:**
    - `dags/output/coto_screenshot.png`
    - `dags/output/coto_page_source.html`
    - Task logs in Airflow UI.
