from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .models import Note, Dream
from .forms import TaskForm, DreamForm


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

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
        tasks = Note.objects.exclude(complete_value=False, author=request.user )
        return render(request, 'task/task_list.html', {'tasks': tasks})

def task_complete_list(request):
    tasks = Note.objects.filter(complete_value=False,  author=request.user )[0:5]
    return render(request, 'task/task_complete_list.html', {'tasks': tasks})


def task_detail(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})


def task_detail_complete(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail_complete.html', {'task' : task})

def dreams_list(request):
    dreams = Dream.objects.all()
    return render(request, 'dream/dreams_list.html', {'dreams' : dreams})


def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.create_date = timezone.now()
            task.save()
    else:
        return redirect('task_detail', pk=task.pk)
        form = TaskForm()
        return render(request, 'task/task_edit.html', {'form' : form})

def dreams_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            dream = form.save(commit=False)
            dream.author = request.user
            dream.save()
            return redirect('dream_detail', pk=dream.pk)
    else:
        form = DreamForm()
        return render(request, 'dream/dream_edit.html', {'form' : form})




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
