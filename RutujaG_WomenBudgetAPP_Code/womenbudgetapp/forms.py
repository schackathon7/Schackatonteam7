from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'username'
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'first name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'last name'
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'email',
            'class': 'form-control',
            'placeholder': 'email'
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'placeholder': 'password'
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class CreateProfileForm(ModelForm):
    age = forms.CharField(widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'placeholder': 'age',

        }
    ))

    class Meta:
        model = Customer
        fields = ['age']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'password', 'type':'password'}))
