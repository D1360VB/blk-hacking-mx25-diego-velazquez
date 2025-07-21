# **BlackRock Challenge - Autoahorro e Inversión**

Este proyecto implementa un sistema de **auto-ahorro e inversión de remanentes de redondeo a multiplos de 100 en gstos** utilizando **FastAPI** en el backend y un **frontend ligero en HTML + JS**.  
Simula cómo los redondeos de transacciones y ciertas reglas de inversión  impactan en el ahorro a largo plazo, aplicando restricciones y cálculos de interés compuesto ajustados por inflación.

---

 **Características**
- **API REST (FastAPI)** con endpoints para:
  - Parsear y validar transacciones.
  - Filtrar por periodos de inversión (q, p, k).
  - Calcular rendimientos en **Planes Personales de Retiro (PPR)** y **fondos iShares IVV**.
  - Mostrar métricas de rendimiento y performance.
- **Frontend visual** con formulario para:
  - Ingresar transacciones (`datetime`, `amount`).
  - Invocar los endpoints desde un panel de prueba.
- **Contenedorizado con Docker** para una ejecución rápida.
- **Documentación interactiva con Swagger** en `http://localhost:5477/docs`.


---

 **Requisitos previos**
- **Docker** >= 20.x
- **Docker Compose** >= 1.29
- Navegador 


 **Cómo ejecutar el proyecto**

 **1. Clonar el repositorio**
git clone https://github.com/USUARIO/blackrock-app.git
cd blackrock-app


 **2. Construir y levantar el servicio**

docker-compose up --build

* La API quedará disponible en `http://localhost:5477`.
* Swagger UI: `http://localhost:5477/docs`.

 **3. Probar el frontend**

Abre el archivo:


frontend/index.html


* Desde el navegador podrás agregar transacciones, enviar peticiones al backend y ver los resultados.

 **4. Detener el servicio**


docker-compose down


---

 **Endpoints principales**

* **`/blackrock/challenge/v1/transactions:parse`**
  Recibe `{date, amount}`, calcula `ceiling` (redondeo) y `remanent`.

* **`/blackrock/challenge/v1/transactions:validator`**
  Valida transacciones en base al sueldo y restricciones de PPR.

* **`/blackrock/challenge/v1/transactions:filter`**
  Filtra transacciones según periodos `q`, `p`, `k`.

* **`/blackrock/challenge/v1/returns:ppr`** y **`/returns:ishares`**
  Calcula rendimientos y proyecciones hasta los 65 años, ajustando por inflación.

* **`/blackrock/challenge/v1/performance`**
  Muestra métricas de ejecución, uso de memoria y threads.

---

 **Ejemplo rápido de uso**

**Request:**


{
  "transactions": [
    { "datetime": "2025-07-01T14:30", "amount": 235.5 },
    { "datetime": "2025-07-03T09:15", "amount": 980.25 }
  ]
}


**cURL:**

bash
curl -X POST "http://localhost:5477/blackrock/challenge/v1/transactions/parse" \
-H "Content-Type: application/json" \
-d '{"transactions":[{"datetime":"2025-07-01T14:30","amount":235.5},{"datetime":"2025-07-03T09:15","amount":980.25}]}'


---

 **Tecnologías**

* **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic.
* **Frontend:** HTML5, JavaScript, Bootstrap.
* **Contenedores:** Docker, Docker Compose.
---


