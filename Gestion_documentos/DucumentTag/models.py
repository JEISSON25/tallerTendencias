from django.db import models

class DocumentTag(models.Model):
    documento = models.ForeignKey(Document, on_delete=models.CASCADE)
    etiqueta = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.documento.nombre} - {self.etiqueta.nombre}"
