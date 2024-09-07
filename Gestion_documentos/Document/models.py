from django.db import models

class Document(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='documents/')
    fecha_carga = models.DateTimeField(auto_now_add=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre