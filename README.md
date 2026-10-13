# Red Social de Aficiones

Proyecto desarrollado con **Django** como parte del módulo de Django del **Máster en Desarrollo Full Stack de Conquer Blocks**.

## Descripción

Esta aplicación consiste en una mini red social temática en la que los usuarios pueden registrarse, iniciar sesión, crear publicaciones, seguir a otros usuarios e interactuar mediante comentarios y likes.

El muro principal muestra las publicaciones propias y las publicaciones de los usuarios seguidos.

La aplicación está desplegada en **Render**, utiliza **PostgreSQL** como base de datos de producción y **Cloudinary** para almacenar las imágenes de las publicaciones y los perfiles.

## Aplicación desplegada

El proyecto se encuentra publicado y puede utilizarse desde el navegador.

**Enlace a la aplicación:** https://proyecto1-django.onrender.com

**Repositorio de GitHub:** https://github.com/Beacm96/Proyecto1_Django

La aplicación permite registrarse, iniciar sesión y probar sus funcionalidades.

**Nota:** El servicio web utiliza el plan gratuito de Render, por lo que la primera carga puede tardar después de un periodo de inactividad. La disponibilidad también depende de que la base de datos permanezca activa.

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

- **User:** modelo de usuario de Django.
- **Profile:** información adicional del usuario, biografía, aficiones y avatar.
- **Post:** publicaciones creadas por los usuarios.
- **Comment:** comentarios en las publicaciones.
- **Like:** interacciones de los usuarios con las publicaciones.
- **Follow:** relaciones de seguimiento entre usuarios.

## Tecnologías utilizadas

### Desarrollo

- Python
- Django
- HTML
- CSS
- Pillow

### Bases de datos

- SQLite: utilizada durante el desarrollo local.
- PostgreSQL: utilizada en el entorno de producción.

### Despliegue y almacenamiento

- **Render:** alojamiento y ejecución de la aplicación Django.
- **Cloudinary:** almacenamiento de las imágenes de perfil y publicaciones.
- **GitHub:** control de versiones y repositorio del código fuente.

## Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/Beacm96/Proyecto1_Django.git
```

### 2. Entrar en la carpeta del proyecto

```bash
cd Proyecto1_Django
```

### 3. Crear un entorno virtual

```bash
python3 -m venv venv
```

### 4. Activar el entorno virtual

En macOS/Linux:

```bash
source venv/bin/activate
```

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar las variables de entorno

El proyecto utiliza variables de entorno para gestionar la configuración y las credenciales de forma segura.

Variables utilizadas en producción:

- `SECRET_KEY`
- `DEBUG`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `DATABASE_URL`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`

Para ejecutar el proyecto localmente es necesario configurar las variables requeridas por `settings.py`.

No se deben incluir contraseñas, claves privadas ni credenciales reales en el repositorio.

### 7. Aplicar las migraciones

```bash
python manage.py migrate
```

### 8. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Funcionalidades principales

### Publicaciones

Los usuarios autenticados pueden crear publicaciones con texto e imagen.

Las imágenes se almacenan mediante Cloudinary en el entorno de producción.

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

## Tests

El proyecto incluye tests para comprobar:

- Creación de publicaciones
- Seguir usuarios
- Dejar de seguir usuarios
- Añadir y eliminar likes
- Visualización de publicaciones de usuarios seguidos en el muro

Para ejecutar los tests:

```bash
python manage.py test
```

Para comprobar la configuración de Django:

```bash
python manage.py check
```

## Despliegue en producción

La aplicación se encuentra desplegada en Render, conectada al repositorio de GitHub.

La configuración de producción utiliza:

- **Render Web Service:** ejecuta la aplicación Django y permite acceder a ella mediante una URL pública.
- **Render PostgreSQL:** almacena los datos de usuarios, perfiles, publicaciones, comentarios y relaciones.
- **Cloudinary:** almacena las imágenes subidas por los usuarios.
- **Variables de entorno:** permiten gestionar la configuración y las credenciales sin incluirlas directamente en el código.

El proyecto utiliza `DEBUG=False` en producción.

**URL pública:** https://proyecto1-django.onrender.com

## Autor

Proyecto realizado como ejercicio académico del módulo de Django del Máster en Desarrollo Full Stack de Conquer Blocks.