from django.db import models
# Create your models here.

class User_mod_pos(models.Model):
	email = models.EmailField(unique=True)
	contraseña = models.CharField(max_length=100)
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	es_admin=models.BooleanField(default=False)
	biografia = models.TextField(blank=True)
	cumpleaños = models.DateField(blank=True, null=True)
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)
		