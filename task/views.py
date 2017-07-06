from django.shortcuts import render

from .models import Note


def task_list(request):
    tasks = Note.objects.filter(complete_value=False)
    return render(request, 'task/task_list.html', {'tasks': tasks})


# Create your views here.
