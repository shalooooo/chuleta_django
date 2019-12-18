### Chuleta Django ###

# instalacion de django
pip install django

# iniciar proyecto
django-admin startproject nombre_proyecto

# crear una app
python manage.py startapp nombre_app

# crear una app con nombre core usando la version 3 de python
python3 manage.py startapp core

# luego de crear una app se debe 'instalar' en el PROJECT, para eso se debe agregar a la lista INSTALLED_APPS en el archivo 'settings.py', al final de esta

# correr servidor virtual para montar la app
python manage.py runserver

# para las urls de la aplicacion se debe crear dentro de la APP un archivo de nombre 'urls.py' e importar el contenido de su semajante del PROJECT sin el primer import
# ahi se definiran las rutas de la aplicacion

# para añadir un layout se debe crear una carpeta de nombre 'templates' en la carpeta de la APP (core), ahi se guardaran los archivos HTML de la app
# para localizar archivos estaticos se crea un directorio dentro de una APP de nombre 'static'...
# ... y dentro de esta se crea una carpeta del nombre de la APP...
# ... y dentro de esta se crean las carpetas CSS, JS y IMG

-MAIN_PROJECT
	-APP:core
		-__pycache__
		-migrations
		-static
			-core
				-css
				-js 
				-img
		-templates
			-core
				-base.html
				-home.html
		-__init__
		-admin.py
		-apps.py
		-models.py
		-tests.py
		-urls.py
		-views.py
	-PROJECT:project
		-__pycache__
		-__init__.py
		-settings.py
		-urls.py
		-wsgi.py
	-manage.py
	-db.sqlite3

# en base.html se pegara el codigo del template deseado y luego se dividira con blockes del framework Django, esto para modularizar la pagina y programarla por partes separadas
-base.html
	{% block nombre_blocke %}
	{% endblock nombre_blocke %}
-home.html
	{% extends 'core/base.html' %}
	{% block nombre_blocke %}
	{% endblock nombre_blocke %}

# para las vistas se debe agregar una funcion en el archiv 'views.py' que reciba el requerimiento 'request' y retorne con la funcion 'render()' dos parametros, primero el mismo 'request' y como segundo parametro la ruta de la vista 'core/home.html'
def home(request):
    return render(request, 'core/home.html')


# para las rutas de la aplicacion se creara un archivo llamado 'urls.py' en la carpeta de la APP:core en este caso 
from django.urls import path
from .views import home

urlspatterns = [
	path('', home, name="home")
]

# para mapear las rutas recien hechas se debe modificar el archivo 'urls.py' pero del PROJECT

from django.contrib import admin
from django.urls import path, include

urlspatterns = [
	path('', include('core.urls')),
	path('admin/', admin.site.urls)
]


# se debe modificar el archivo 'settings.py' de la carpeta PROJECT, en la lista llamada INSTALLED_APPS se debe agregar al final las apps
INSTALLED_APPS = [
	...,
	'core',
]
 
# para llamar recursos estaticos se debe agregar dentro del html
{% load static %}

# para añadir las rutas dentro de los tags html los archivos css o js
{% static 'core/css/estilo.css' %}
{% static 'core/jss/bootstrap.min.js' %}
{% static 'core/img/foto.jpg' %}

# para crear los tags 'a href' se debe usar la funcion 'url'
{% url 'alias_ruta' %}# path:name="home"
{% url 'home' %}

fin video 1 shoro moise
__________________________________________________________________________________________________
inicio video 2 shoro moise

# en el archivo 'models.py' para crear los modelos

class NombreModelo(models.Model):
	# django agrega un id autoincremental a todos los modelos por defecto
	nombre_atributo_string = models.CharField(max_lenght=200, unique=True)
	nombre_atributo_entero = models.IntegerField()

class NombreModelo2(models.Model):
	nombre_llave_foranea = models.ForeingKey(NombreModelo, on_delete=models.CASCADE)

# para realizar la migracion se debe ejecutar el siguiente comando
python manage.py makemigrations
python manage.py migrate 

# para ir al backend por defecto que crea el framework django se debe ir a la url /admin
# para registrar los modelos que se desean agregar al backend se deben agregar las siguientes lineas en el archivo 'admin.py' 

from django.contrib import admin
from .models import NombreModelo, NombreModelo2

admin.site.register(NombreModelo)
admin.site.register(NombreModelo2)

# para entrar en el login creado por defecto del framework django se debe crear el usuarion administrador desde la consola
python manage.py createsuperuser
Username:
Password:

# para personalizar el backend administrador se debe agregar los metodos to string a los modelos
class NombreModelo(models.Model):
	nombre_atributo_string = models.CharField(max_lenght=200, unique=True)
	nombre_atributo_entero = models.IntegerField()

	def __str__(self):
		return self.nombre_atributo_string

class NombreModelo2(models.Model):
	nombre_llave_foranea = models.ForeingKey(NombreModelo, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_llave_foranea

# para cambiar el idioma del backend administrador se debe cambiar el 
LANGUAGE_CODE = 'es'
LANGUAGE_CODE = 'en-us'

# para cambiar los metadatos de los modelos se puede agregar una clase dentro de la clase del modelo en el archivo models.py

class NombreModelo(models.Model):
	.
	.
	.
	class Meta:
		verbose_name = "NombreModelo"
		verbose_name_plural = "NombreModelos"

# para cambiar el nombre del titulo de los cruds en el panel admin de django se debe ir al archivo 'apps.py'
# se debe agregar el verbose_name dentro de la clase CoreConfig
class CoreConfig(AppConfig):
	name = 'APP'
	verbose_name = 'nuevo nombre'

# para cargar la configuracion recien hecha se debe hacer en el archivo 'settings.py'
INSTALLED_APPS = [
	...,
	'core.apps.CoreConfig',
]


















##########################################################################
# instalacion admin lte 2 layout
pip install django-adminlte2
# agregar en installed apps
INSTALLED_APPS = [
    # Any apps which will override adminlte's templates (i.e. your apps)
    ...

    # The general purpose templates
    'django_adminlte',

    # Optional: Skin for the admin interface
    'django_adminlte_theme',

    # Any apps which need to have their templates overridden by adminlte
    'django.contrib.admin',
    ...
]
##########################################################################