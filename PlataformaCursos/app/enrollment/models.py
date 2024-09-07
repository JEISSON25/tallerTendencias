from django.db import models
from ..course.models import Course
from ..user.models import User

# Create your models here.
class Enrollment(models.Model):
    class Meta: 
        verbose_name = "Enrollment" 
        verbose_name_plural = "Enrollments" 
  
    idCourse = models.ForeignKey ( 
    Course, 
    verbose_name="Course", 
    on_delete=models.CASCADE, 
    null=True, 
    blank=True 
    ) 
    idUser = models.ForeignKey ( 
    User, 
    verbose_name="User", 
    on_delete=models.CASCADE, 
    null=True, 
    blank=True 
    ) 

    fecha =models.DateField("Fecha de inscripción")

    def __str__(self):
        return f'{Course.nombre} {User.nombre}{User.apellido}'
   