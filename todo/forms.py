from django import forms
from django.forms import ModelForm
from todo.models import Todo
from bootstrap_datepicker_plus import DatePickerInput


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'memo', 'important', 'expire']
        widgets = {
            'expire': DatePickerInput(format='%d-%m-%Y'),
        }
