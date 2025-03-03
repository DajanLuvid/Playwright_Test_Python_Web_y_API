import asyncio
from playwright.async_api import async_playwright, expect

async def metodo():
    async with async_playwright() as p:
        # Inicia el navegador Firefox en modo no oculto
        browser = await p.firefox.launch(headless=False)
        
        # Crea un nuevo contexto de navegación
        context = await browser.new_context()
        
        # Inicia la grabación de la sesión con capturas de pantalla, instantáneas y código fuente
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        
        # Abre una nueva página en el navegador
        page = await context.new_page()
        
        # Establece el tamaño de la ventana del navegador
        await page.set_viewport_size({"width": 1800, "height": 1200})
        
        # Navega a la página de prueba
        await page.goto("https://demoqa.com/buttons")
        
        # Realiza un desplazamiento vertical de 300 píxeles
        await page.evaluate("window.scrollBy(0, 300)")
        
        # Localiza el tercer botón con el texto "Click Me" y hace clic en él
        boton = page.locator("text=Click Me").nth(2)
        await boton.click()
        
        # Espera 1 segundo después del clic
        await page.wait_for_timeout(1000)
        
        # Toma una captura de pantalla después del clic
        await page.screenshot(path="screenshots/clicks_1.png")
        
        # Verifica que el mensaje de clic dinámico aparezca correctamente
        await expect(page.locator("#dynamicClickMessage")).to_have_text("You have done a dynamic click")
        
        # Localiza el primer botón con el texto "Click Me" y hace doble clic en él
        boton = page.locator("text=Click Me").nth(0)
        await boton.dblclick()
        
        # Espera 1 segundo después del doble clic
        await page.wait_for_timeout(1000)
        
        # Toma una captura de pantalla después del doble clic
        await page.screenshot(path="screenshots/clicks_2.png")
        
        # Verifica que el mensaje de doble clic aparezca correctamente
        await expect(page.locator("#doubleClickMessage")).to_have_text("You have done a double click")
        
        # Detiene la grabación de la sesión y guarda el archivo de rastreo
        await context.tracing.stop(path="logs/trace_clicks.zip")
        
        # Cierra el navegador
        await browser.close()

# Ejecuta la función asincrónica
asyncio.run(metodo())

# Ejecutarlo en la terminal
# python inputs/clicks.py