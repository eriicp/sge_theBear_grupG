# sge_theBear_grupG

# Projecte FastAPI - DAM1 - Hugo Murillo Caparrós

## Configuració del projecte
### 1. Crear estructura de directoris

Afegir un fitxer `__init__.py` buit a cada carpeta.

![alt text](image.png)

### 2. Crear `connect.py`

Fitxer situat a `database/connect.py` per gestionar la connexió a la base de dades amb `psycopg2`

![alt text](image-1.png)

### 3. Crear `read_sch.py`

Fitxer situat a `schema/read_sch.py` per transformar dades en diccionari.

![alt text](image-2.png)

### 4. Crear `read.py`

Fitxer situat a `services/read.py` amb la lògica per gestionar les consultes.

![alt text](image-3.png)

### 5. Crear `main.py`
Fitxer principal que actua com a controlador.

![alt text](image-4.png)

## Execució del projecte
Executar el servidor amb:

python -m uvicorn main:app --reload


![alt text](image-5.png)

Accedir a `http://127.0.0.1:8000` per veure l'API.

![alt text](image-6.png)

Per veure la documentació accedim a `http://127.0.0.1:8000/docs`.

![alt text](image-7.png)

