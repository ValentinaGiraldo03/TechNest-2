from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Client, Administrator

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ClientRegisterForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['address', 'phone']

class AdministratorRegisterForm(forms.ModelForm):
    class Meta:
        model = Administrator
        fields = []
