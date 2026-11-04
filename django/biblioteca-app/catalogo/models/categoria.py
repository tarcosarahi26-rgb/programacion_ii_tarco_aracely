from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        app_label = 'catalogo'
        verbose_name = "categoría"
        verbose_name_plural = "categorías"  
        ordering = ['nombre']