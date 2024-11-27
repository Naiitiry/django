from django.forms import ModelForm, DateInput, TextInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model=Todo
        exclude=('date',)
        widgets={
            'estimated_end':DateInput(attrs={'type':'date'}),
            'date':DateInput(format=('%Y-%m-%d'),attrs={'type':'date'}),
            'priority':TextInput(attrs={'type':'number','min':1,'max':5})
        }