from django.contrib import admin
from django.urls import path, re_path
from articles import views

urlpatterns = [
    path('', views.archive, name='archive'),
    path('admin/', admin.site.urls),
    re_path(r'^article/(?P<article_id>\d+)/$', views.get_article, name='get_article'),
]