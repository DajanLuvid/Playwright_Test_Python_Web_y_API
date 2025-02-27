import re
from playwright.sync_api import Page, expect


def test_example(browser):
    context = browser.new_context(ignore_https_errors=True)  # Configurar para ignorar HTTPS
    page = context.new_page()  # Crear la página con ese contexto

    page.goto("https://identidad.reniec.gob.pe/")  
    #page.pause()

    # Validar que estamos en la página correcta
    expect(page).to_have_url(re.compile(r"identidad\.reniec\.gob\.pe"))
    expect(page).to_have_title(re.compile(r"Registro Nacional de Identificación y Estado Civil - Reniec", re.I))

    # Pasamos el mouse sobre "CONÓCENOS"
    page.get_by_role("button", name="CONÓCENOS").hover()

    # Hacemos clic en "Iniciativas y recursos"
    page.get_by_role("button", name="Iniciativas y recursos").click()

    # Hacemos clic en "Servicios RENIEC en consulados"
    page.get_by_role("link", name="Servicios RENIEC en consulados").click()

    # Esperamos la apertura de una nueva pestaña y validamos la URL
    with page.expect_popup() as page1_info:
        page.locator("#buttonCardImage137014").click()
    page1 = page1_info.value  

    # Validar que la nueva página cargó correctamente
    expect(page1).to_have_url(re.compile(r"consulado\.pe/paginas/Inicio\.aspx"))

    # Buscamos "cuenca"
    page1.get_by_role("textbox", name="Búsqueda...").click()
    page1.get_by_role("textbox", name="Búsqueda...").fill("cuenca")
    
    # Hacemos clic en "Realiza búsquedas"
    page1.get_by_role("link", name="Realiza búsquedas").click()

    print("URL actual:", page1.url)
    # page.pause() #depurar

    # Esperamos la apertura del popup y validamos que sea la de Cuenca para dar clic
    with page1.expect_popup() as page2_info:
        page1.get_by_role("dialog", name="Oficinas Consulares").locator("iframe").content_frame.get_by_role("link", name="Cuenca").click()
    page2 = page2_info.value  

    # Validamos que la página cargada es la del consulado de Cuenca
    expect(page2).to_have_url(re.compile(r"cuenca", re.I))
    expect(page2.locator("#nombreConsulado")).to_be_visible()

    # Regresar a la pestaña inicial
    page.bring_to_front()

    # Esperar 3 segundos
    page.wait_for_timeout(3000) 
