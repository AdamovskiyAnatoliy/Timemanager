<<<<<<< HEAD
from django import forms

from .models import Note

=======
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
s
from .models import Note


>>>>>>> bedf95df6b0b4272b0871764a837c8c76dcafaea
class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('must_complete_before','task')
<<<<<<< HEAD
=======

>>>>>>> bedf95df6b0b4272b0871764a837c8c76dcafaea
