 
# Proyecto Final - Informatorio 2da Etapa

Este repositorio corresponde al trabajo final desarrollado para el Informatorio 2da Etapa. El proyecto consiste en una aplicación web tipo BLOG con funcionalidades específicas y perfiles de usuario. A continuación, se detallan los requisitos, especificaciones y restricciones del proyecto.

## Integrantes del Grupo

- Matías Efrén Nedel
- Martín Luciano Vallejos
- Gonzalo Exequiel Flores
- Guillermo Toffaletti

  ## Usuarios pythonanywhere
| Rol    | Usuario   | Contraseña          |
|--------|-----------|---------------------|
| Admin  | admin     | salioelsol          |
| Miembro| miembro   | caelsolentubalcon   |

# Especificaciones y Restricciones

## Perfiles de Usuario:

1. **Super Admin (Django):**
   - Otorgado por Django para la administración del sistema.

2. **Colaborador:**
   - Cargar, Editar y Eliminar artículos, fotos asociadas a los mismos y comentarios de los demás
usuarios.
   - Categorizar artículos.

3. **Visitante:**
   - Navegar por la web.
   - Filtrar los diferentes posteos.
   - Leer artículos
   - Registrarse y loguearse en la web.

4. **Miembro o Usuario Registrado:**
   - Navegar por la web.
   - Comentar en los artículos.
   - Editar o eliminar sus propios comentarios.
   - Desloguearse.

## Aplicacion Web - Tipo BLOG:

1. **Inicio o Portada:**
   - Muestra una selección de las publicaciones más recientes o destacadas.
   - Proporciona una visión general del contenido del blog y permite a los visitantes explorar fácilmente las ultimas actualizaciones..

2. **Categorías:**
   - Divide el contenido del blog en categorías temáticas claras y organizadas.

3. **Acerca de:**
   - Proporciona información sobre el blog y su propósito.
   - Puede incluir una breve descripción del equipo detrás del blog.

4. **Contacto:**
   - Ofrece a los visitantes una forma de ponerse en contacto con el equipo.
   - Puede incluir un formulario de contacto, dirección de correo electrónico o enlaces a redes sociales.

   **IMPORTANTE:** Las secciones mencionadas son requisitos mínimos; el equipo de desarrolladores puede agregar más secciones según sus preferencias.

## Funcionalidades del Proyecto:

1. **Artículos:**
   - Crear, leer, editar y eliminar artículos.

2. **Comentarios:**
   - Crear, leer, editar y eliminar comentarios.

3. **Filtrar Publicaciones por:**
   - Categoría.
   - Antigüedad (ascendente y descendente).
   - Orden alfabético (ascendente y descendente).

4. **Gestión de Usuarios:**
   - Registrarse, loguearse y desloguearse.



## Instrucciones de Configuración y Ejecución:
1. Clona el repositorio: git clone https://github.com/gtoffa/blog_grupo9
2. Configura el entorno virtual
```bash
   # macOS/Linux
   # Es posible que necesites ejecutar  `sudo apt-get install python3-venv` en sistemas operativos basados ​​en Debian
   python3 -m venv .venv

   # Windows
   # También puedes usar  `py -3 -m venv .venv`
   python -m venv .venv
```
3. Activa el entorno virtual:
```bash
   # macOS/Linux
   source .venv/bin/activate

   # Windows
   .venv\Scripts\activate
```
4. Instala las dependencias: pip install -r requirements.txt
5. Crea la base de datos blog_grupo9 en Mysql 8.0
```sql
CREATE SCHEMA `blog_grupo9`;
```
6. Configura la base de datos en el archivo blog/settings/local.py
7. Realiza las migraciones: python manage.py migrate
8. Crea un superusuario: python manage.py createsuperuser


## Ejecución:
1. Ejecuta el servidor local:
```bash
  python manage.py runserver 
```
2. Accede a la aplicación web desde tu navegador: http://localhost:8000/
