from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre 
