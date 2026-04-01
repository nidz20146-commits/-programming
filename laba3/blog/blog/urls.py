from django.contrib import admin
from django.urls import path
from articles import views 

urlpatterns = [
    # Главная страница - архив всех статей
    path('', views.archive, name='archive'),
    
    # Админка
    path('admin/', admin.site.urls),
]