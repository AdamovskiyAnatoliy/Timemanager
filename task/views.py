from django.shortcuts import render, get_object_or_404

from .models import Note


def task_list(request):
    tasks = Note.objects.filter(complete_value=False)
    return render(request, 'task/task_list.html', {'tasks': tasks})

"""def task_complete(request):
    tasks = Note.objects.filter(complete_value=True)
    return render(request, 'task/task_complete.html', {'tasks': tasks})
"""


def task_detail(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

# Create your views here.
