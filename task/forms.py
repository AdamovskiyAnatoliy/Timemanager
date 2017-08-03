from django import forms
from django.forms.widgets import DateTimeInput, TextInput
from django.forms import ModelForm

from .models import Note, Dream


class TaskForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('task', 'must_complete_before',)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task'].widget= TextInput(
            attrs = {
                    'class': 'form-control',
                    'placeholder': 'Exemle: GO shoping'
            }
        )
        self.fields['must_complete_before'].widget = DateTimeInput(
            attrs = {
                    'class': 'form-control',
                    'type': 'datetime',
                    'placeholder': 'Exemle: 2017-07-16 05:06:06'
            }
        )


class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ('detail_dream', 'priority_dream', 'my_dream',)

    def __init__(self, *args, **kwargs):
        super(DreamForm, self).__init__(*args, **kwargs)

        self.fields['my_dream'].widget.attrs['class'] = 'form-control'
        self.fields['detail_dream'].widget.attrs['class'] = 'form-control'
        self.fields['priority_dream'].widget.attrs['class'] = 'form-control'
