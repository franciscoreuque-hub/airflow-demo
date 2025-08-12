# Airflow + Selenium Web Scraping Demo

[![Airflow](https://img.shields.io/badge/Airflow-2.8.1-blue)](https://airflow.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3.9-orange)](https://docs.docker.com/compose/compose-file/compose-versioning/)

---

## Summary
**Short description for a CV / portfolio:**  
> *Currently I'm running a containerized Apache Airflow DAG that uses Selenium to scrape product data from a dynamic e-commerce site.*

---

## What this demo shows
- How to run a containerized **Airflow** stack (webserver + scheduler + Postgres) with a **Selenium** standalone Chrome service.
- How to call a remote WebDriver from an Airflow PythonOperator.
- Basic handling of dynamic/lazy-loaded pages (scrolling + screenshots + saving page source).

---

## Repo structure
├── dags/
│ ├── coto_verificar_productos.py
│ └── output/ # screenshots & page sources (create this before running)
├── Dockerfile
├── docker-compose.yml
└── README.md
