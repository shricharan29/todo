from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

# Create your views here.
def home(request):
    tasks = Todo.objects.filter(user=request.user.id)

    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        action = request.POST.get('action')

        if action == 'done':
            task = Todo.objects.get(id=task_id)
            task.done = True
            task.save()
        elif action == 'pending':
            task = Todo.objects.get(id=task_id)
            task.done = False
            task.save()

    data = {'tasks': tasks if len(tasks) != 0 else "none", 'user':request.user}
    return render(request, 'base/home.html',data)

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.instance.user = request.user
            todo_form.save()
        return redirect('home')

    todo_form = TodoForm()
    data = {'todo_form':todo_form, 'action':'Add'}
    return render(request, 'base/todo.html',data)

@login_required(login_url='login')
def edit(request, pk):
    todo_obj = Todo.objects.get(pk=pk)

    if request.method == 'POST':
        todo_form = TodoForm(request.POST, instance=todo_obj)
        if todo_form.is_valid():
            todo_form.save()
        return redirect('home')
    
    todo_form = TodoForm(instance = todo_obj)
    data = {'todo_form':todo_form, 'action':'Edit'}
    return render(request, 'base/todo.html',data)

@login_required(login_url='login')
def delete_task(request, pk):
    task = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')

    data = {'task':task}
    return render(request, 'base/delete.html',data)

@login_required(login_url='login')
def delete_completed(request):
    if request.method == 'POST':
        comp_task = Todo.objects.filter(done=True)
        for task in comp_task:
            task.delete()
        return redirect('home')
        
    data = {'task':'all completed task'}
    return render(request, 'base/delete.html',data)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        next = request.GET.get('next') if request.GET.get('next') != None else 'home'

        if user is not None:
            login(request,user)
            return redirect(next)
        
    data = {}
    return render(request, 'base/login.html', data)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        messages.error(request,"You are not authenticated")
        return redirect('home')
    
def register(request):
    if request.method == 'POST':
        user = UserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            return redirect('login')
        else:
            messages.error(request,"Error: Form invalid or user already registered")
            return redirect('home')
    data = {'form': UserCreationForm()}
    return render(request, 'base/register.html',data)