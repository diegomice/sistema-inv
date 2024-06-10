# Importa el módulo de administración de Django y funciones para manejar rutas URL.
from django.contrib import admin

# Importa la función `path` para definir rutas y `include` para incluir otras configuraciones de URL.
from django.urls import path, include

# Importa el módulo `views` desde la aplicación `productos`.
from productos import views

# Define la lista `urlpatterns` que contiene las rutas URL que se configurarán para el proyecto.
urlpatterns = [
    # Define una ruta para la interfaz de administración.
    # Cuando la URL comienza con 'admin/', se utiliza la interfaz de administración de Django.
    path('admin/', admin.site.urls),
    
    # Define una ruta raíz ('').
    # Incluye las rutas definidas en el archivo `urls.py` de la aplicación `productos`.
    # Esto permite modularizar las rutas de URL de la aplicación `productos`.
    path('',include('productos.urls')),
]
