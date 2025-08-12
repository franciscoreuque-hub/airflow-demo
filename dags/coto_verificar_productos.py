from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

OUTPUT_DIR = "/opt/airflow/dags/output"

def verificar_productos():
    url = "https://www.cotodigital.com.ar/sitios/cdigi/categoria/catalogo-almacén-golosinas-alfajores/_/N-1njwjm5"

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    # If needed, run headless:
    # options.add_argument('--headless=new')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )

    driver.get(url)
    time.sleep(5)  # wait for dynamic content

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Save screenshot & HTML for debugging
    driver.save_screenshot(os.path.join(OUTPUT_DIR, 'coto_screenshot.png'))
    with open(os.path.join(OUTPUT_DIR, 'coto_page_source.html'), 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # Scroll to load lazy content
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(10):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Locate product elements (adjust selector to actual site)
    productos = driver.find_elements(By.CSS_SELECTOR, 'h3.nombre-producto')
    if productos:
        print(f"Productos encontrados: {len(productos)}")
        for i, prod in enumerate(productos[:5], 1):
            print(f"{i}. {prod.text}")
    else:
        print("No se encontraron productos visibles.")

    driver.quit()

with DAG(
    'coto_verificar_productos',
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['scraping']
) as dag:
    verificar_task = PythonOperator(
        task_id='verificar_productos',
        python_callable=verificar_productos
    )
