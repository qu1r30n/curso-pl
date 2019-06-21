"""Platzigram URLs module."""

from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static	
from posts import views as posts_views


urlpatterns = [
	path('admin/', admin.site.urls),
    path('posts/', posts_views.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

