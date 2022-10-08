from django.urls import path
from . import views

urlpatterns = [
    path('', views.Inicio, name='inicio'),
    path('login', views.Login, name='login'),
    path('edit_borrar', views.Edit_borrar, name='edit_borrar'),
    path('inscribirse', views.Inscribirse, name='inscribirse'),
    path('borrar', views.Borrar, name='borrar'),
    path('edit', views.Edit, name='edit'),
    path('inicio', views.Inicio, name='inicio'),
]