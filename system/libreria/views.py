from django.shortcuts import render
from django.http import HttpResponse


def Inicio(request):
    return render(request, 'paginas/inicio.html')
def Login (request):
    return render(request, 'paginas/login.html')
def Recuperarpass(request):
    return render(request, 'paginas/recuperarpass.html')
def Inscribirse(request):
    return render(request, 'paginas/inscribirse.html')
