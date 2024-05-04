from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Creando las vistas del proyecto.

#HOME
def home(request):
    return render(request, 'home.html')

#INVENTARIOS
def inventarios(request):
    return render(request, 'inventarios.html')

#Lista_repuestos
def lista_repuestos(request):
    return render(request, 'lista_repuestos.html')

#ListaDe Chequeo Piso 1
def listaDeChequeo2(request):
    return render(request, 'listaDeChequeo2.html')

#ListaDe Chequeo Piso 2
def listaDeChequeo(request):
    return render(request, 'listaDeChequeo.html')

#LIsta de chequeoo Piso 3
def listaDeChequeo3(request):
    return render(request, 'listaDeChequeo3.html')


#LIsta de chequeo Cubierta
def cubierta(request):
    return render(request, 'cubierta.html')






#Registro de usuarios
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error":'Contraseña Incorrecta'
        })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'tasks.html',{'tasks': tasks})

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    
    return render(request, 'tasks.html',{'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request,'create_task.html', {
            'form': TaskForm
        })
    else:
        try: 
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user    
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'tasks.html', {
                'form': TaskForm,
                "error": 'POr favor diligencie los datos'
            })

@login_required        
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request,'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'task_detail.html', {'task': task, 'form': form, 'error': "Error actualizando los datos"})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')
    
@login_required    
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')    

@login_required 
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:             
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o Clave Incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')