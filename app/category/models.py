from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)

    def __str__(self) -> str:
        return f"{self.nombre}"