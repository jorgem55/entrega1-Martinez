from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    moto=models.CharField(max_length=20)
    fecha_compra = models.DateField(null=True)
    