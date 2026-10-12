# Red Social de Aficiones

Proyecto desarrollado con Django como parte del módulo de Django del Máster en Desarrollo Full Stack.

## Descripción

Esta aplicación consiste en una mini red social temática en la que los usuarios pueden registrarse, iniciar sesión, crear publicaciones, seguir a otros usuarios e interactuar mediante comentarios y likes.

El muro principal muestra las publicaciones propias y las publicaciones de los usuarios seguidos.

## Funcionalidades

- Registro de usuarios
- Inicio y cierre de sesión
- Creación automática de perfil
- Edición de perfil
- Biografía y aficiones en el perfil
- Avatar de usuario
- Publicaciones con texto e imagen
- Sistema de comentarios
- Sistema de likes
- Seguir usuarios
- Dejar de seguir usuarios
- Contador de seguidores
- Contador de usuarios seguidos
- Muro con publicaciones propias y de usuarios seguidos

## Modelos principales

- User
- Profile
- Post
- Comment
- Like
- Follow

## Tecnologías utilizadas

- Python
- Django
- HTML
- CSS
- SQLite
- Pillow

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Beacm96/Proyecto1_Django.git
```

Entrar en la carpeta del proyecto:

```bash
cd Proyecto1_Django
```

Crear un entorno virtual:

```bash
python3 -m venv venv
```

Activar el entorno virtual en macOS/Linux:

```bash
source venv/bin/activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

## Migraciones

Aplicar las migraciones de Django:

```bash
python manage.py migrate
```

## Ejecutar el proyecto

Iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

Después abrir en el navegador:

```text
http://127.0.0.1:8000/
```

## Tests

Ejecutar los tests del proyecto:

```bash
python manage.py test
```

Comprobar que Django no detecta errores de configuración:

```bash
python manage.py check
```

## Funcionalidades principales

### Publicaciones

Los usuarios autenticados pueden crear publicaciones con texto e imagen.

### Perfiles

Cada usuario dispone de un perfil en el que puede añadir una biografía, sus aficiones y una imagen de avatar.

### Seguidores

Los usuarios pueden seguir y dejar de seguir a otros usuarios.

### Muro

El muro principal muestra las publicaciones propias y las publicaciones de los usuarios seguidos.

### Likes

Los usuarios autenticados pueden añadir o eliminar un like de una publicación.

### Comentarios

Los usuarios autenticados pueden comentar en las publicaciones.

## Tests incluidos

El proyecto incluye tests para comprobar:

- Creación de publicaciones
- Seguir usuarios
- Dejar de seguir usuarios
- Añadir y eliminar likes
- Visualización de publicaciones de usuarios seguidos en el muro

## Autor

Proyecto realizado como ejercicio académico del módulo de Django.