# Importa funciones y clases necesarias de Django.
from django.shortcuts import render, HttpResponse

# Importa el modelo Producto del archivo models.py de la aplicación actual.
from .models import Producto

# Definición de las vistas.

def inicio(request):
    # Esta vista renderiza y devuelve el contenido del template 'inicio.html'.
    return render(request, 'inicio.html')


