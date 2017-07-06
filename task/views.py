from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Note
from .forms import UserRegistrationForm


class RegistrationView(CreateView):
    """ Custom view for registering students """
    form_class = UserRegistrationForm
    template_name = 'registration/register.html'
    success_url = 'main'

    def form_valid(self, form):
        user = form['user'].save()
        student = form['student'].save(commit=False)
        student.user = User.objects.get(username=user.username)
        student.save()
        new_user = authenticate(username=form['user'].cleaned_data['username'],
                                password=form['user'].cleaned_data['password1'])
        login(self.request, new_user)
        return redirect(reverse(self.success_url))




def main(request):
    return render(request, 'main.html', {})

def task_list(request):
    tasks = Note.objects.filter(complete_value=False)
    return render(request, 'task/task_list.html', {'tasks': tasks})

def task_detail(request, pk):
    task = get_object_or_404(Note, pk=pk)
    return render(request, 'task/task_detail.html', {'task': task})

def task_complete_list(request):
    tasks = Note.objects.filter(complete_value=True)
    return render(request, 'task/task_complete_list.html', {'tasks': tasks})

# Create your views here.
