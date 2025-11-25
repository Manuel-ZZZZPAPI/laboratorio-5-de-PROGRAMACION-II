# laboratorio-5-de-PROGRAMACIÓN-II
# API REST con Flask y SQLite

## Descripción
Este proyecto implementa una API REST utilizando Flask y SQLite.  
La API gestiona un recurso llamado user, permitiendo operaciones CRUD(Crear, Leer, Actualizar y Eliminar).

El objetivo es demostrar la construcción estructurada de una API, manejo de las rutas, validaciones, respuesta en formato JSON y pruebas atraves de Postman.


## Objetivos del Proyecto
- Diseñar e implementar una API REST funcional.
- Utilizar Flask como microframework para construir servicios web.
- Persistir datos mediante SQLite sin necesidad de un servidor adicional.
- Aplicar buenas prácticas de arquitectura y organización de código.
- Probar endpoints mediante herramientas como Postman.

## Estructura del Proyecto
```
Carpeta api_flask
-app.py                # Archivo principal con rutas y lógica de negocio
-db.py           # Conexión a SQLite y creación de tablas
-README.md             # Documentación del proyecto
-structureDB.sql    # Script SQL para crear la tabla 'users'
```


##Tecnologías Utilizadas
- **Python 3.9+**
- **Flask**
- **SQLite3**
- **Postman** para pruebas


## Instalación y Configuración
### 1. Clonar el repositorio
```bash
git clone https://github.com/tuproject/api_flask_sqlite.git
cd api_flask_sqlite
```

### 2. Crear un entorno virtual
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```
### 3. Crea structureDB.sql con el esquema 
-- structureDB.sql
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT,
    email TEXT UNIQUE,
    creado_en TEXT DEFAULT (datetime('now','localtime'))
);

### 4. Crea db.py. 
''' Implementa funciones get(id=None), post(data), put(id, data), delete(id) y gestión de errores.

### 5. Crea app.py con las rutas y respuestas JSON
´´Usamos int para <int:user_id> (valida automáticamente).
´´POST /users no recibe id en la ruta (se autogenera).
´´Manejo explícito de errores con códigos HTTP.

### 6. Ejecutar la API
```bash
python app.py
```

### 7. URL base
```
http://127.0.0.1:5000
```
## Base de Datos
La base de datos SQLite se genera automáticamente al ejecutar el proyecto por primera vez.

## Endpoints Disponibles
### Obtiene todos los usuarios
**GET** `/users`

### Obtiene un usuario por ID
**GET** `/users/<id>`

### Crear un usuario
**POST** `/users`
```json
{
  "nombre": "Adrian",
  "apellido": "Pino",
  "email": "adrianpino@gmail.com",
  "edad": 15
}
```

### Actualizar usuario
**PUT** `/users/<id>`

### Eliminar usuario
**DELETE** `/users/<id>`

---

## Pruebas con Postman

## Pruebas GET en Postman

### GET /users — Obtener todos los usuarios
Método: GET
Endpoint: http://127.0.0.1:5000/users
![Obtener todos los usuarios](img/postman_get1.png)<img width="567" height="298" alt="image" src="https://github.com/user-attachments/assets/c8eae416-11fe-451b-bc4c-fb832c629207" />


GET /users/<id> — Obtener usuario por ID
Método: GET
Endpoint: http://127.0.0.1:5000/users/8
![Obtener usuario por ID](img/postman_get2.png)<img width="567" height="305" alt="image" src="https://github.com/user-attachments/assets/cc665e2c-db37-41e6-9ab5-71111e5f12c5" />


Error en GET (cuándo id no existente)
Método: GET
Endpoint: http://127.0.0.1:5000/users/1
![Cuándo id no existente](img/postman_get3.png)<img width="567" height="295" alt="image" src="https://github.com/user-attachments/assets/4421ca1c-055f-46a4-9500-f8cc2a5f3a6b" />


## Pruebas con POST
POST /users — Crear un nuevo usuario
Método: POST
Endpoint: http://127.0.0.1:5000/users
![Crear un nuevo usuario](img/postman_post1.png)<img width="567" height="298" alt="image" src="https://github.com/user-attachments/assets/b7106ef3-fa4d-4fe8-bbe3-1f277d01de60" />


![Error en POST(gmail duplicado)](img/postman_post2.png)<img width="567" height="266" alt="image" src="https://github.com/user-attachments/assets/1c27cb3f-543c-47c1-90a1-6d0f1034bf19" />


![Error en POST(faltan datos)](img/postman_post3.png)<img width="567" height="580" alt="image" src="https://github.com/user-attachments/assets/2e2c9b29-fe67-4434-b6ed-9311652471d0" />


## Pruebas con PUT
PUT /users/<id> — Actualizar un usuario existente
Método: PUT
Endpoint: http://127.0.0.1:5000/users/8
![foto(sin actualizar página del navegador)](img/postman_put1.png)<img width="567" height="289" alt="image" src="https://github.com/user-attachments/assets/3ab8878a-5b77-45ee-a888-4f954f3dd01b" />


![foto(actualizando la página del navegador)](img/postman_put2.png)<img width="567" height="289" alt="image" src="https://github.com/user-attachments/assets/28381ea8-5f7c-4f62-9183-db929038532f" />


Error en PUT (Cuando id no existente)
Método: PUT
Endpoint: http://127.0.0.1:5000/users/1
![(Cuando id no existente)](img/postman_put3.png)<img width="567" height="289" alt="image" src="https://github.com/user-attachments/assets/73f138ec-5748-40e5-b5af-1e1cf15e39a3" />



## Pruebas con  DELETE
DELETE /users/<id> — Eliminar un usuario
Método: DELETE
Endpoint: http://127.0.0.1:5000/users/9
![Foto(sin actualizar página del navegador)](img/postman_delete1.png)<img width="567" height="298" alt="image" src="https://github.com/user-attachments/assets/c38e8662-5004-4175-bd4b-01fb97bc1dcf" />

![Foto(actualizando página del navegador)](img/postman_delete2.png)<img width="567" height="298" alt="image" src="https://github.com/user-attachments/assets/f76a6b32-3703-468d-9a9f-8b798d39fd84" />


Error en DELETE(cuando id no existente)
Método: DELETE
Endpoint: http://127.0.0.1:5000/users/1
![DELETE](img/postman_delete3.png)<img width="567" height="298" alt="image" src="https://github.com/user-attachments/assets/67a71595-6319-472f-bfa7-07cdefbe035d" />
