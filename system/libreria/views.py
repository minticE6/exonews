from django.shortcuts import render
from django.http import HttpResponse
from .models import explanetas, userandpassword

def Inicio(request):
    Explanetas = explanetas.objects.all()
    return render(request, 'paginas/inicio.html')
def Login (request):
    Userandpassword = userandpassword.objects.all()
    return render(request, 'paginas/login.html')
def Recuperarpass(request):
    return render(request, 'paginas/recuperarpass.html')
def Inscribirse(request):
    return render(request, 'paginas/inscribirse.html')
