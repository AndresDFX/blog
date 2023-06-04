# Proyecto Blog

Este proyecto es una aplicación web para gestionar entradas de blog, comentarios y likes. Permite a los administradores gestionar todos los recursos, a los editores gestionar entradas, comentarios y likes, y a los bloggers crear y gestionar sus propias entradas, comentarios y likes.

## Características

- Registro y autenticación de usuarios.
- Roles de usuario: administrador, editor y blogger.
- Gestión de entradas de blog: creación, edición, eliminación y consulta.
- Gestión de comentarios en las entradas: creación, edición, eliminación y consulta.
- Sistema de likes en las entradas y comentarios.
- Filtros y ordenamiento de entradas.
- API RESTful para acceder a los recursos.

## Tecnologías utilizadas

- Django: framework web de Python.
- Django REST Framework: para construir la API RESTful.
- PostgreSQL: base de datos relacional para almacenar los datos.
- Python 3.10.4

## Instalación

1. Clona este repositorio en tu máquina local.
2. Crea y activa un entorno virtual para el proyecto.
3. Instala las dependencias del proyecto utilizando el archivo `requirements.txt`.
4. Configura la conexión a la base de datos en el archivo `settings.py`.
5. Realiza las migraciones de la base de datos utilizando el comando `python manage.py migrate`.
6. Carga los grupos iniciales utilizando el comando `python manage.py loaddata groups.json`.
7. Para crear un usuario ejecutar el comando `python manage.py create_user --username=admin@letsdoitnow.us --first_name=Editor --last_name=Editor --email=admin@letsdoitnow.us --group=ADMINS `.
8. Inicia el servidor de desarrollo con el comando `python manage.py runserver`.

## Uso

Una vez que el servidor de desarrollo esté en funcionamiento, puedes acceder a la aplicación en tu navegador web utilizando la dirección `http://localhost:8000`. Aquí puedes registrarte como usuario y comenzar a utilizar las funcionalidades según tu rol.

En el repositorio se encuentra una collection de postman con todos los servicios.
