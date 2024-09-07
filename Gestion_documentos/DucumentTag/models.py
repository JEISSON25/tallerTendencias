from django.db import models
from django.contrib.auth.models import User
from models import Document
from models import Tag

class DucumentTag(models.Model):
    documento = models.ForeignKey(Document, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.documento.nombre} - {self.etiqueta.nombre}"
