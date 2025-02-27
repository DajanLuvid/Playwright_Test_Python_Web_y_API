# Importamos Playwright para controlar el navegador
from playwright.sync_api import sync_playwright  

# Importamos pytest para escribir y ejecutar pruebas
import pytest  

# Para obtener variables de entorno
import os

# Definimos las variables con la URL y los mensajes esperados en la prueba
url = "https://www.saucedemo.com/"
titulo_esperado = "Swag Labs"
message_inventory_error = "Epic sadface: You can only access '/inventory.html' when you are logged in."

# Obtenemos el tamaño de la ventana desde variables de entorno
# Si no están definidas, usamos valores por defecto (1920x1080)
WINDOW_WIDTH = int(os.getenv("WINDOW_WIDTH", 1920))
WINDOW_HEIGHT = int(os.getenv("WINDOW_HEIGHT", 1080))

# FIXTURE: Configuración del navegador
@pytest.fixture
def browser():
    # Iniciamos Playwright
    with sync_playwright() as p:  
        # Lanzamos el navegador en modo visible (headless=False)
        browser = p.chromium.launch(headless=False)  
        # Dejamos el navegador listo para usar en las pruebas
        yield browser  
        # Cerramos el navegador después de ejecutar las pruebas
        browser.close()  

# FIXTURE: Configuración de la página
@pytest.fixture
def page(browser):
    # Creamos un nuevo contexto (como una nueva sesión del navegador)
    context = browser.new_context()  
    # Abrimos una nueva página en el navegador
    page = context.new_page()  
    # Establecemos el tamaño de la ventana según las variables de entorno
    page.set_viewport_size({"width": WINDOW_WIDTH, "height": WINDOW_HEIGHT})  
    # Dejamos la página lista para las pruebas
    yield page  
    # Cerramos la página después de la prueba
    page.close()  

# PRUEBA 1: Verificar que el título de la página es el esperado
def test_title(page):
    # Navegamos a la página de prueba
    page.goto(url)  
    # Comprobamos que el título de la página sea "Swag Labs"
    assert page.title() == titulo_esperado  

# PRUEBA 2: Intentar acceder a la página de inventario sin iniciar sesión
def test_inventory_page(page):
    # Intentamos acceder a la página de inventario sin iniciar sesión
    page.goto(url + "inventory.html")  
    # Verificamos que se muestre el mensaje de error esperado
    assert page.inner_text("h3") == message_inventory_error  
