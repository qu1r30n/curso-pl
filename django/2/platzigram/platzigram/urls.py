from django.urls import path
from platzigram.vistas import *


urlpatterns = [
    path('fecha_y_hora/',fecha_y_hora),
    path('ordenar_num/',ordenar),
    path('hola_mundo/<str:nombre>/<int:edad>/', hola_mundo)
    
]
