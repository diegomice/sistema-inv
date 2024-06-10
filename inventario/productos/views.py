# Importa funciones y clases útiles desde Django.
from django.shortcuts import render, HttpResponse, get_object_or_404

# Importa el modelo `Producto` desde el archivo `models.py` en el directorio actual.
from .models import Producto

# Define una vista llamada `inicio` que renderiza la plantilla 'inicio.html'.
def inicio(request):
    return render(request, 'inicio.html')

# Define una vista llamada `lista_productos` que obtiene todos los productos del modelo `Producto` y los pasa a la plantilla 'productos.html'.
def lista_productos(request):
    # Obtiene todos los productos del modelo `Producto`.
    productos_list = Producto.objects.all()
    # Renderiza la plantilla 'productos.html' y pasa la lista de productos como contexto.
    return render(request, 'productos.html', {'productos': productos_list})

# Define una vista llamada `detalle` que toma un argumento `producto_id`, obtiene el producto correspondiente del modelo `Producto` o muestra una página 404 si no se encuentra.
def detalle(request, producto_id):
    # Obtiene el producto correspondiente al `producto_id` proporcionado o muestra una página 404 si no se encuentra.
    producto = get_object_or_404(Producto, id=producto_id)
    # Renderiza la plantilla 'detalle.html' y pasa el producto como contexto.
    return render(request, 'detalle.html', {'producto': producto})
