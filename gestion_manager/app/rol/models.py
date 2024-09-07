from django.db import models

class Rol(models.Model):
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
    name = models.CharField('Nombre', max_length=100)
    
    def __str__(self):
        return self.name
