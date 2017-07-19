from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Note, Dream, TopDream
from .forms import TaskForm, DreamForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def task_list(request):
    if str(request.user) == 'AnonymousUser':
        return render(request, 'home.html', {})
    else:
        tasks = Note.objects.filter(complete_value=False, author=request.user )
        return render(request, 'task/task_list.html', {'tasks': tasks})

def task_complete_list(request):
    tasks = Note.objects.filter(complete_value=True,  author=request.user )[0:5]
    return render(request, 'task/task_complete_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_detail_complete(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail_complete.html', {'task' : task})

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.create_date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'task/task_edit.html', {'form' : form})

def task_edit(request, pk):
    task = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_edit.html', {'form': form})


def dreams_new(request):
    if request.method == "POST":
        form = DreamForm(request.POST)
        if form.is_valid():
            dream = form.save()
            dream.author = request.user
            dream.save()
            print('Hood')
            return redirect('dream_detail', pk=dream.pk)
    else:
        form = DreamForm()
    return render(request, 'dream/dream_edit.html', {'form' : form})

def dreams_list(request):
    dreams = Dream.objects.all()
    return render(request, 'dream/dreams_list.html', {'dreams' : dreams})

def dream_detail(request, pk):
    dream = get_object_or_404(Dream, pk=pk)
    return render(request, 'dream/dream_detail.html', {'dream':dream})


def top_dream(request):
    top = Dream.objects.all()
    return render(request, 'dream/top_dream.html', {'top' : top })
