from .models import Passes
from django.forms import ModelForm, TextInput

class PassForm(ModelForm):
    class Meta:
        model = Passes
        fields = ["title", "login", "password"]
        widgets = {"title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название'
        }),
                   "login": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
        }),
                   "password": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        }),
        }