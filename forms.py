from django.forms import ModelForm
from .models import Usuarios

class UserCreateForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ('usuario', 'email', 'senha')
