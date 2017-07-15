from django import forms
from django.forms.widgets import DateTimeInput

from .models import Note, Dream


class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('task', 'must_complete_before')

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task'].widget.attrs['class'] = 'form-control '
        self.fields['must_complete_before'].widget = DateTimeInput(attrs={
            'class':'vDateField', 'id':'id_must_complete_before_0',
            'name':'must_complete_before_0', 'size':'10', 'type':'text',
            })



class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ('detail_dream', 'priority_dream', 'my_dream', )

    def __init__(self, *args, **kwargs):
        super(DreamForm, self).__init__(*args, **kwargs)

        self.fields['my_dream'].widget.attrs['class'] = 'form-control'
        self.fields['detail_dream'].widget.attrs['class'] = 'form-control'
        self.fields['priority_dream'].widget.attrs['class'] = 'form-control'
