from django.db import models 
from ..course.models import Course 

class Lesson(models.Model): 
    class Meta:  
        verbose_name = "Lesson"  
        verbose_name_plural = "Lesson"  

    nombre = models.CharField("Nombre", max_length=100) 
    contenido = models.CharField("Contenido ", max_length=200) 

    idCourse = models.ForeignKey (  
    Course,  
    verbose_name="Course",  
    on_delete=models.CASCADE,  
    null=True,  
    blank=True  
    )

    def __str__(self): 
        return f'{self.nombre} {self.contenido} {Course.nombre}'