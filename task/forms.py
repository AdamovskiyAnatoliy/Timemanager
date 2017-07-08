from django import forms

from .models import Note

class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('task', 'must_complete_before',)
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task'].widget.attrs['class'] = 'form-control '
        self.fields['must_complete_before'].widget.attrs['class'] = 'form-control'
