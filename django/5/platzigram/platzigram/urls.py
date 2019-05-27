from django.urls import path
from django.contrib import admin

from platzigram.vistas import *
from posts.views import *


urlpatterns = [
    path("admin/", admin.site.urls),

    path('fecha_y_hora/',fecha_y_hora),
    path('ordenar_num/',ordenar),
    path('hola_mundo/<str:nombre>/<int:edad>/', hola_mundo),
    path('posts/',lista_posts)
]
