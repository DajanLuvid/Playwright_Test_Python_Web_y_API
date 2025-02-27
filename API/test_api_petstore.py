from typing import Generator
import pytest
import json  # Necesario para convertir el diccionario de Python a formato JSON
from playwright.sync_api import Playwright, APIRequestContext  # Importa Playwright para manejar peticiones HTTP

# URL base de la API del Petstore
url_base = "https://petstore.swagger.io/v2"

# Código de la mascota que se usará en las pruebas
codigo_mascota = 99

# Configuración del fixture de pytest para gestionar el contexto de las peticiones API
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    # Crea un nuevo contexto de petición con la URL base
    request_context = playwright.request.new_context(base_url=url_base)
    yield request_context  # Devuelve el contexto para su uso en las pruebas
    request_context.dispose()  # Libera los recursos del contexto al finalizar

# Prueba para crear una nueva mascota en la API
def test_post_pet(api_request_context: APIRequestContext) -> None:
    # Datos de la nueva mascota en formato diccionario
    data_input = {
        "id": codigo_mascota,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Chesterson",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # Convierte el diccionario a formato JSON
    json_data = json.dumps(data_input)

    # Realiza la petición POST para agregar la nueva mascota
    new_post = api_request_context.post(
        "/v2/pet",
        data=json_data,
        headers={"Content-Type": "application/json"}  # Define el encabezado para JSON
    )

    # Verifica si la respuesta es exitosa (Código 200 OK)
    assert new_post.status == 200, f"Error: Código de estado {new_post.status}"
    
    # Muestra la respuesta en la consola
    mostrar_response(new_post, "POST")

# Prueba para obtener la información de una mascota
def test_get_pet(api_request_context: APIRequestContext) -> None:
    # Realiza la petición GET para obtener los datos de la mascota creada
    new_get = api_request_context.get(
        f"/v2/pet/{codigo_mascota}"  # Usa el ID de la mascota en la URL
    )

    # Verifica si la respuesta es exitosa (Código 200 OK)
    assert new_get.status == 200, f"Error: Código de estado {new_get.status}"
    
    # Muestra la respuesta en la consola
    mostrar_response(new_get, "GET")

# Prueba para actualizar los datos de la mascota
def test_update_pet(api_request_context: APIRequestContext) -> None:
    # Datos actualizados de la mascota
    data_input = {
        "id": codigo_mascota,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Chesterson ACTUALIZADO",  # Se cambia el nombre
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "available"
    }

    # Convierte el diccionario a JSON
    json_data = json.dumps(data_input)

    # Realiza la petición PUT para actualizar los datos de la mascota
    new_update = api_request_context.put(
        f"/v2/pet/{codigo_mascota}",
        data=json_data,
        headers={"Content-Type": "application/json"}  # Define el encabezado para JSON
    )

    # Verifica si la respuesta es exitosa (Código 200 OK)
    assert new_update.status == 200, f"Error: Código de estado {new_update.status}"
    
    # Muestra la respuesta en la consola
    mostrar_response(new_update, "UPDATE")

# Prueba para eliminar una mascota de la API
def test_delete_pet(api_request_context: APIRequestContext) -> None:
    # Realiza la petición DELETE para eliminar la mascota
    new_delete = api_request_context.delete(
        f"/v2/pet/{codigo_mascota}"
    )

    # Verifica si la respuesta es exitosa (Código 200 OK)
    assert new_delete.status == 200, f"Error: Código de estado {new_delete.status}"
    
    # Muestra la respuesta en la consola
    mostrar_response(new_delete, "DELETE")

# Función auxiliar para imprimir el estado y el contenido de la respuesta
def mostrar_response(response, METODO):
    print("\n\n------------------------------------------------------------------")
    print(f"{METODO} response status: {response.status}")  # Imprime el código de estado
    print(f"{METODO} response text: {response.text()}")  # Imprime el cuerpo de la respuesta
    print("------------------------------------------------------------------")



# EJECUTAR CON 
# pytest -s test_api_petstore.py