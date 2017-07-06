from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Note
from .forms import TaskForm


def task_list(request):
    tasks = Note.objects.filter(complete_value=False)
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

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
    return render(request, 'task/task_edit.html', {'form': form})



def task_edit(request, pk):
    task = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.create_date = timezone.now()
            task.save()
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_edit.html', {'form': form})

def task_complete_list(request):
    tasks = Note.objects.filter(complete_value=True)
    return render(request, 'task/task_complete_list.html', {'tasks': tasks})

# Create your views here.
