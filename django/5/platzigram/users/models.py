"""User models."""

from django.contrib.auth.models import User
from django.db import models


class perfil(models.Model):
	"""modelo de perfil
	proxy model that extends the base data
	with other information."""

	usuario = models.OneToOneField(User,on_delete=models.CASCADE)
	sitioweb= models.URLField(max_length=200, blank=True)
	biografia= models.TextField(blank=True)
	num_tel= models.CharField(max_length=20, blank=True)

	imagen = models.ImageField(upload_to="usuarios/imaenes", blank=True, null=True)

	creado = models.DateTimeField(auto_now_add=True)
	modificado= models.DateTimeField(auto_now=True)

	def __str__(self):
		"""return username. """
		return self.user.username