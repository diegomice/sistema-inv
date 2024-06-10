# Importa la función `path` del módulo `django.urls` para definir rutas de URL.
from django.urls import path

# Importa el módulo `views` del paquete actual. `views` es donde se definen las funciones que manejarán las solicitudes a las diferentes rutas.
from . import views

# Define la lista `urlpatterns` que contiene las rutas URL que se configurarán para este módulo.
urlpatterns = [
    # Define una ruta vacía ('') que se refiere a la raíz del sitio web.
    # Asocia esta ruta con la función `inicio` que se encuentra en `views`.
    # El nombre de la ruta es 'inicio', lo que permite referirse a esta ruta por su nombre en otras partes de la aplicación.
    path('', views.inicio, name='inicio'),
]
