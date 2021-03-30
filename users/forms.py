from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import FileInput
from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',  'email']
    email = forms.EmailField(label='Ввдите Email: ',
                             required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Ввдите Email'})
                             )
    username = forms.CharField(
        label='Ввдите логин: ',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ввдите логин'})
    )
    password1 = forms.CharField(
        label='Ввдите пароль: ',
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль: ',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username',  'email']
    email = forms.EmailField(label='Ввдите Email: ',
                             required=True,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Ввдите Email'})
                             )
    username = forms.CharField(
        label='Ввдите логин: ',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Ввдите логин'})
    )


class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['img']
    img = forms.ImageField(label='Загрузит фото',
                           required=False,
                           widget=forms.FileInput
                           )
