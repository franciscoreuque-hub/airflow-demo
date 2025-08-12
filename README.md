# Airflow + Selenium Web Scraping Demo

[![Airflow](https://img.shields.io/badge/Airflow-2.8.1-blue)](https://airflow.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green)](https://www.selenium.dev/)
[![Docker Compose](https://img.shields.io/badge/Docker%20Compose-v3.9-orange)](https://docs.docker.com/compose/compose-file/compose-versioning/)

---

## Summary
> *This repo was thought for demostrate how to get running a containerized Apache Airflow DAG that uses Selenium to scrape product data from a dynamic e-commerce site.*

---

## What this demo shows
- How to run a containerized **Airflow** stack (webserver + scheduler + Postgres) with a **Selenium** standalone Chrome service.
- How to call a remote WebDriver from an Airflow PythonOperator.
- Basic handling of dynamic/lazy-loaded pages (scrolling + screenshots + saving page source).

---

## 1. Getting airflow up and running
run docker-compose up --build
This will start:
Airflow webserver
Airflow scheduler
Postgres metadata database
Selenium Standalone Chrome (for browser automation)
You can access the Airflow webserver at http://localhost:8080.
The default username and password are: admin/admin

---

## 2. Initializing Airflow
Before running any DAGs, initialize the Airflow database and create an admin user:
docker-compose run airflow-init

---
## 3. Running the scraping DAG
The main DAG is located at:
dags/coto_verificar_productos.py

# It performs the following:
Opens a Coto Digital product category page.
Scrolls down to load dynamic content.
Saves a screenshot (coto_screenshot.png) and the HTML page source (coto_page_source.html) in dags/output/.
Logs the first 5 product names found.
# Steps to run it:
Go to the Airflow webserver.
Enable the coto_verificar_productos DAG.
Click the trigger button to run it manually.
Open the Graph View to see task progress.
Check Logs to see product names in console output.
View generated files in dags/output/.

----

## 4. Output example
Productos encontrados: 20
1. Alfajor TERRABUSI Triple Clásico 70g
2. Alfajor HAVANNA Chocolate
3. Alfajor TITA
4. Alfajor MILKA Oreo
5. Alfajor JORGITO Triple

----

## 5. Additional notes
Selenium service runs at http://selenium:4444/wd/hub and is accessed from Airflow tasks via Remote WebDriver.

I still have to do some testing to get sure the data is exctracted too with headless instance
