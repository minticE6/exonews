from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('login', views.Login, name='login'),
    path('recuperarpass', views.Recuperarpass, name='recuperarpass'),
    path('inscribirse', views.Inscribirse, name='inscribirse'),
]