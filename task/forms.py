from django import forms

from .models import Note

class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('task','must_complete_before',)
