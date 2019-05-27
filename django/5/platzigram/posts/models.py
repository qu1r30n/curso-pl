from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    es_administrador= models.BooleanField(default=False)

    descripcion = models.TextField(blank=True)
    
    cumpleaños = models.DateField(blank=True, null=True)

    chequeo = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        """regresa_email"""
        return(self.email)