from .models import TestTask
from django.forms import ModelForm, TextInput, Textarea

class TestTaskForm(ModelForm):
    class Meta:
        model = TestTask
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }