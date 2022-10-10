from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('login', views.Login, name='login'),
    path('borrar', views.Edit_borrar, name='borrar'),
    path('inscribirse', views.Inscribirse, name='inscribirse'),
    path('Borrar', views.Borrar, name='Borrar'),
    path('inicio', views.Inicio, name='inicio'),
    path('edit', views.Edit, name='edit'),
]