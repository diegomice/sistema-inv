# productos/models.py

from django.db import models

class Producto(models.Model):
    # Campos del modelo (por ejemplo, nombre, precio, etc.)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    # ...

    def __str__(self):
        return self.nombre
