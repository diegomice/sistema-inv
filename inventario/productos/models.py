# Importa el módulo de modelos de Django.
from django.db import models

# Define la clase `Producto` que hereda de `models.Model`, representando una tabla en la base de datos.
class Producto(models.Model):
    # Define un campo para el nombre del producto, limitado a 100 caracteres.
    nombre = models.CharField(max_length=100)
    # Define un campo para la descripción del producto, de tipo texto (no hay límite de longitud).
    descripcion = models.TextField()
    # Define un campo para el precio del producto, con un máximo de 10 dígitos y 2 decimales.
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # Define un campo para la imagen del producto, que se almacenará en el directorio 'productos/'.
    # El campo puede ser nulo (null=True) y puede quedar en blanco (blank=True) en el formulario.
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    # Método que devuelve una representación legible del objeto Producto (nombre del producto).
    def __str__(self):
        return self.nombre
