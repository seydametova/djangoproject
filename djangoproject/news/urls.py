from django.urls import path, include
from . import views

"""Прописываю обработку страниц"""
urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update'),    # Остлеживаю динамический параметр(целое число:primary key(сам параметр))
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='news_delete')
]