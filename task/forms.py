from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
s
from .models import Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('must_complete_before','task')

