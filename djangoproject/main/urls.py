from django.urls import path, include
from . import views

"""Подключаю url-адреса, которые буду отслеживать"""
urlpatterns = [
    path('', views.get_index, name='home'),
    path('blog', views.about, name='blog'),
]