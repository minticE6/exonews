from django.shortcuts import render
from .models import explanetas, userandpassword
from .forms import Userandpasswordform

def Inicio(request):
    Explanetas = explanetas.objects.all()
    return render(request, 'paginas/inicio.html', {'Explanetas': Explanetas})
def Login (request):
    
    return render(request, 'paginas/login.html')
def Recuperarpass(request):
    return render(request, 'paginas/recuperarpass.html')

def Inscribirse(request):
    formulario = Userandpasswordform(request.POST or None)
    return render(request, 'paginas/inscribirse.html', {'formulario': formulario})
