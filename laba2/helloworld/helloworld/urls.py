# coding: utf-8
from django.contrib import admin
from django.urls import path
from flatpages import views

urlpatterns = [
    # Главная страница (корень сайта)
    path('', views.home, name='home'),
    
    # Новый адрес /hello/ — та же функция
    path('hello/', views.home, name='hello'),
    
    # Админка
    path('admin/', admin.site.urls),
]