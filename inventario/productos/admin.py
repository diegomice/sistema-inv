# Importa el módulo de administración de Django.
from django.contrib import admin

# Importa el modelo `Producto` desde el archivo `models.py` en el directorio actual.
from .models import Producto

# Registra el modelo `Producto` en la interfaz de administración de Django.
admin.site.register(Producto)
