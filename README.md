# Proyecto API de Películas

Este proyecto es una API de películas que utiliza Flask y MySQL, y está completamente dockerizado para facilitar la configuración y ejecución.

## Requisitos

- Docker
- Docker Compose

## Configuración

### Clonar el Repositorio

Clona este repositorio en tu máquina local:

```sh
git clone git@github.com:wcossior/Api_Movies_Python.git
cd Api_Movies_Python
```
### Configuracion de las variables de entorno:

- `MYSQL_ROOT_PASSWORD`: La contraseña para el usuario root de MySQL.  
- `MYSQL_DATABASE`: El nombre de la base de datos que se creará.  
- `MYSQL_USER`: El nombre de usuario para la base de datos MySQL.  
- `MYSQL_PASSWORD`: La contraseña para el usuario especificado en `MYSQL_USER`.  
- `SQLALCHEMY_DATABASE_URI`: La URI de la base de datos que SQLAlchemy usará para conectarse a MySQL.

### Ejecutar el siguiente comando para construir y levantar los contenedores:

```sh
docker-compose up --build
```

### Algunos ejemplos para hacer un post

    {
        "Autor": "Gabriel García Márquez",
        "Descripcion": "Cien años de soledad es una novela escrita por el autor colombiano.",
        "Fecha_de_Estreno": "Tue, 30 May 1967 00:00:00 GMT",
        "ID": 2
    },
    {
        "Autor": "J.K. Rowling",
        "Descripcion": "Harry Potter y la piedra filosofal es la primera novela de la serie de Harry Potter.",
        "Fecha_de_Estreno": "Thu, 26 Jun 1997 00:00:00 GMT",
        "ID": 3
    },
    {
        "Autor": "George Orwell",
        "Descripcion": "1984 es una novela distópica publicada en 1949.",
        "Fecha_de_Estreno": "Wed, 08 Jun 1949 00:00:00 GMT",
        "ID": 4
    }

### Endpoints de la API

- **POST** `/movies`: Crear una nueva película en la base de datos.
- **GET** `/movies`: Obtener una lista de todas las películas en la base de datos.
- **PUT** `/movies/<id>`: Actualizar los detalles de una película específica en la base de datos.
- **DELETE** `/movies/<id>`: Eliminar una película específica de la base de datos.
