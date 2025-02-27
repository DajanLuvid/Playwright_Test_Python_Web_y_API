# Importamos asyncio para manejar funciones asíncronas
import asyncio
# Importamos Playwright en su versión asíncrona y la función expect para realizar validaciones
from playwright.async_api import async_playwright, expect

# Definimos una función asíncrona principal
async def main():
    # Iniciamos Playwright y usamos el contexto "async with" para gestionar recursos
    async with async_playwright() as p:
        
        # Lanzamos un navegador Chromium con la opción headless=False (para ver la ejecución)
        browser = await p.chromium.launch(headless=False)
        # Creamos un nuevo contexto de navegación (similar a una nueva sesión)
        context = await browser.new_context()
        # Iniciamos la captura de trazas para depuración (incluyendo capturas, snapshots y código fuente)
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # Abrimos una nueva pestaña en el contexto creado
        page = await context.new_page()
        # Establecemos el tamaño de la ventana del navegador
        await page.set_viewport_size({"width": 1800, "height": 1200})
        # Navegamos a la página de prueba de checkboxes
        await page.goto("https://demoqa.com/checkbox")

        # ---- Acciones ----
        # Marcamos el checkbox de "Home"
        await page.check('label[for="tree-node-home"]')
        # Tomamos una captura de pantalla y la guardamos en la carpeta "screenshots"
        await page.screenshot(path="screenshots/checkboxes.png")

        # ---- Validaciones ----
        # Verificamos si el checkbox "Home" está marcado
        await page.is_checked('label[for="tree-node-home"]') is True
        # Validamos que el texto en el elemento con id "result" sea el esperado
        await expect(page.locator("#result")).to_have_text(
            "You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile"
        )

        # ---- Finalización ----
        # Detenemos la captura de trazas y guardamos el archivo en la carpeta "logs"
        # Para ver el log debemos escribir en la terminal: playwright show-trace logs/trace.zip
        await context.tracing.stop(path="logs/trace.zip")
        # Cerramos el navegador
        await browser.close()

# Ejecutamos la función principal de forma asíncrona
asyncio.run(main())
