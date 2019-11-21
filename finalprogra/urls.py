from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.lista_peliculas, name ='lista_peliculas'),
    url(r'^$', views.menu_nueva, name='menu_nueva'),
    ]
