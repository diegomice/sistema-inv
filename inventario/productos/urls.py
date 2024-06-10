# Importa la función `path` desde el módulo `django.urls`.
from django.urls import path

# Importa las vistas desde el archivo `views.py` en el directorio actual.
from . import views

# Define la lista `urlpatterns` que contiene las rutas URL que se configurarán para la aplicación.
urlpatterns = [
    # Define una ruta raíz ('') que corresponderá a la vista `inicio` en el archivo `views.py`.
    # También se asigna el nombre 'inicio' a esta ruta para su identificación en otros lugares del código.
    path('', views.inicio, name='inicio'),

    # Define una ruta 'productos/' que corresponderá a la vista `lista_productos` en `views.py`.
    # También se asigna el nombre 'productos' a esta ruta para su identificación en otros lugares del código.
    path('productos/', views.lista_productos, name='productos'),

    # Define una ruta 'productos/<int:producto_id>/' que corresponderá a la vista `detalle` en `views.py`.
    # `<int:producto_id>` indica que se espera un número entero como parte de la URL, que se pasará a la vista como argumento.
    # También se asigna el nombre 'detalle' a esta ruta para su identificación en otros lugares del código.
    path('productos/<int:producto_id>/', views.detalle, name='detalle'),
]
