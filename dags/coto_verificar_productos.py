from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def verificar_productos():
    url = "https://www.cotodigital.com.ar/sitios/cdigi/categoria/catalogo-almacén-golosinas-alfajores/_/N-1njwjm5"

    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        options=options
    )

    driver.get(url)
    time.sleep(5)  # espera para que cargue contenido dinámico
    # Guardar screenshot para validar visualización
    driver.save_screenshot('/opt/airflow/dags/output/coto_screenshot.png')

    # Guardar HTML actual para inspección
    with open('/opt/airflow/dags/output/coto_page_source.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # Scroll para cargar productos dinámicamente
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(10):
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(3)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

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
