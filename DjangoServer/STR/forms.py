from .models import Ticket
from django.forms import ModelForm, TextInput, Textarea

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["name", "description"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название учебного предмета'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание учебного предмета'
            }),
        }