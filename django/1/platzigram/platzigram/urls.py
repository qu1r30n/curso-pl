from django.urls import path
from platzigram.vistas import *


urlpatterns = [
    path('fecha_y_hora/',fecha_y_hora),
    path('hola_mundo/',hola_mundo)
    
]
