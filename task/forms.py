from django import forms

from .models import Note

class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('must_complete_before','task')
