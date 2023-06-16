from django.db import models

# Create your models here.
class Projecto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    tecnologia = models.CharField(max_length=50)
    fecha_creado = models.DateField(auto_now_add=True)