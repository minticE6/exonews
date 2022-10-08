from django.shortcuts import render, redirect
from .models import explanetas, userandpassword
from .forms import Userandpasswordform

def Inicio(request):
    Explanetas = explanetas.objects.all()
    return render(request, 'paginas/inicio.html', {'Explanetas': Explanetas})

def Login (request):
    return render(request, 'paginas/login.html')

def Edit_borrar(request):
    userid = userandpassword.objects.last()
    userid2 = Userandpasswordform(request.POST or None, request.FILES or None, instance = userid)
    return render(request, 'paginas/edit_borrar.html', {'userid2': userid2})

def Edit(request):
    useredit = userandpassword.objects.last()
    useredit2 = Userandpasswordform(request.POST or None, request.FILES or None, instance = useredit)
    if useredit2.is_valid() and request.POST:
        useredit2.save()
    return redirect('edit_borrar')

def Borrar(request):
    userdelete = userandpassword.objects.last()
    userdelete.delete()
    return redirect('inicio')

def Inscribirse(request):
    formulario = Userandpasswordform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    return render(request, 'paginas/inscribirse.html', {'formulario': formulario})
