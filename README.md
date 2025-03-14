# Pruebas Playwright


## ########
## ########     CONSULTAR CONSULADO EN LA PAGINA DE LA RENIEC
## ########

Prueba automatizada con **Playwright** en Python para validar el flujo de navegación hacia la página del consulado de Cuenca.

## 📌 Requisitos
- Python 3.10 o superior
- pip (administrador de paquetes de Python)

## 📦 Instalación de dependencias
Ejecuta el siguiente comando en la terminal para instalar Playwright y Pytest:

```sh
pip install playwright pytest
```

Después, instala los navegadores necesarios para Playwright:

```sh
playwright install
```

Esto descargará y configurará los navegadores compatibles (Chromium, Firefox y WebKit).

## 🚀 Cómo ejecutar las pruebas
Si quieres correr la prueba de la página del consulado, usa:

```sh
pytest -s codegen_demo_reniec.py
```

## 📂 Estructura del proyecto
```
Pruebas Playwright/
│── API/                  # Pruebas para API REST (si aplica)
│── inputs/               # Archivos de entrada (si aplica)
│── codegen_demo_reniec.py # Prueba automatizada de navegación
│── pytest.ini            # Configuración de pytest
│── README.md             # Documentación del proyecto
```

## ########
## ########     CONSULTAR API DE PETSTORE
## ########

Este proyecto contiene pruebas automatizadas de API utilizando Playwright con Python. Se realizan operaciones de tipo CRUD (Crear, Leer, Actualizar, Eliminar) sobre los servicios de la API Petstore.

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- Playwright para Python
- Pytest para la ejecución de pruebas

Para instalar las dependencias necesarias (en caso no las hayas instalado en el ejemplo anterior), ejecuta:

```sh
pip install playwright pytest
playwright install
```

## Estructura del Proyecto

- `test_api_petstore.py`: Contiene las pruebas para la API Petstore.
- `pytest.ini`: Archivo de configuración para pytest.

## Ejecución de Pruebas

Para ejecutar las pruebas de la API, accede a la caperta **API** usa el siguiente comando:

```sh
pytest -s test_api_petstore.py
```

### Nota Importante

Las pruebas pueden fallar debido a que la API Petstore no es completamente estable para pruebas en simultáneo. Como múltiples usuarios pueden estar probando la API al mismo tiempo, es posible que algunas peticiones sean omitidas o que los datos sean eliminados antes de su validación. Se recomienda ejecutar las pruebas en un entorno aislado o verificar manualmente los resultados en caso de inconsistencias.

---
**Autor:** David Luján

