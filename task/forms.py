from django import forms

from .models import Note, Dream

class TaskForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('task', 'must_complete_before',)

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['task'].widget.attrs['class'] = 'form-control '
        self.fields['must_complete_before'].widget.attrs['class'] = 'form-control'


class DreamForm(forms.ModelForm):
    class Meta:
        model = Dream
        fields = ('my_deream', 'detail_deram', 'priority_dream',)

    def __init__(self, *args, **kwargs):
        super(DreamForm, self).__init__(*args, **kwargs)

        self.fields['my_deream'].widget.attrs['class'] = 'form-control'
        self.fields['detail_deram'].widget.attrs['class'] = 'form-control'
        self.fields['priority_dream'].widget.attrs['class'] = 'form-control'
