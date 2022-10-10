from django.shortcuts import render, redirect
from .models import explanetas, userandpassword
from .forms import Userandpasswordform, Uservalidateform
from .context_processors import mis_variables as varglobal


def Inicio(request):
    Explanetas = explanetas.objects.all()
    usuarios = userandpassword.objects.all()
    return render(request, 'paginas/inicio.html', {'Explanetas': Explanetas, 'usuarios': usuarios})

def Login (request):
    form= Uservalidateform(request.POST)
    if form.is_valid():
        marcax = userandpassword.objects.get(apodo=form.cleaned_data['apodo'])
        marca1 = marcax.id
        print("form validado")
        print("apodo:", form.cleaned_data['apodo'])
        print("contrasena:", form.cleaned_data['contrasena'])
        print(marca1)
        return redirect('inicio')
    else:
        form = Uservalidateform()
        print("no es valido")
    return render(request, 'paginas/login.html', {'form' : form})

def Edit_borrar(request):
    userid = userandpassword.objects.last()
    userid2 = Userandpasswordform(request.POST or None, request.FILES or None, instance = userid)
    return render(request, 'paginas/borrar.html', {'userid2': userid2})

def Edit(request):
    useredit3 = userandpassword.objects.last()
    useredit = userandpassword.objects.get(id=useredit3.id)
    useredit2 = Userandpasswordform(request.POST or None, request.FILES or None, instance = useredit)
    if request.method == 'GET':
        print("cambiar el metodo a post")
    if request.method == 'POST':
        print("metodo en post")
    if useredit2.is_valid() and request.POST:
        useredit2.save()
        return redirect('edit')
    return render(request, 'paginas/edit.html', {'useredit2': useredit2})


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
