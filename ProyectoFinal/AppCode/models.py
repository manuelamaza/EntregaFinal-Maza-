from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Curso(models.Model):
    
    nombre=models.CharField(max_length=40)
    camada=models.IntegerField()

class Estudiante(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()
    profesion=models.CharField(max_length=30)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - mail {self.mail} - Profesión {self.profesion}"


        

