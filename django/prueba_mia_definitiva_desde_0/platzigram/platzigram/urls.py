"""Platzigram URLs module."""

from django.urls import path

	
from posts import views as posts_views


urlpatterns = [

    path('posts/', posts_views.list_posts),
]
