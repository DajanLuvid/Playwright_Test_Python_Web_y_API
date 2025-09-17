# 🚀 Automations with Playwright and Python

Repository with practical examples of **automated tests** in Python using **Playwright**. It includes:  
- a navigation test to access the Consulate page (RENIEC — Cuenca), and  
- CRUD tests for the **Petstore API**.

## 🎯 Goal
Show real (UI + API) flows that are reproducible and easy to run, demonstrating automation and testing skills with Playwright and Pytest.

## ⚙️ Requirements
- Python **3.10+**  
- `pip` (package manager)

## 🧰 Quick Installation
Run in your terminal:
```sh
pip install playwright pytest
playwright install
```

## ▶️ How to Run
- **Web Test (RENIEC):**
    pytest -s codegen_demo_reniec.py

- **API Tests (Petstore):**
    cd API
    pytest -s test_api_petstore.py

## 📂 Project Structure
```sh
Playwright Tests/
│── API/                   # REST API tests
│── inputs/                # Input files (if any)
│── codegen_demo_reniec.py # RENIEC navigation test
│── test_api_petstore.py   # CRUD tests for Petstore
│── pytest.ini             # Pytest configuration
│── README.md              # This file
```

## ⚠️ Important Note about Petstore
The public Petstore API can be unstable when many users test it simultaneously. Some tests may fail due to external conditions. For consistent results, run the tests in a controlled environment, use mocks, or clean up created resources at the end.

## 🛠️ Best Practices
- Always run `playwright install` before executing tests to ensure browsers are installed.  
- Isolate test data when possible (avoid collisions on public APIs).

---

**Author:** David Luján

