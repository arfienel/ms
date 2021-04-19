from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','style':'width:30%;margin:10px'}))
    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control','style':'width:30%;margin:10px'}))
    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(attrs={'class': 'form-control','style':'width:30%;margin:10px'}))
    email = forms.EmailField(label='E-mail',widget=forms.EmailInput(attrs={'class': 'form-control','style':'width:30%;margin:10px'}))

    class Meta:
        model = User
        fields = ('username','email','password1','password2')



class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',max_length=30,widget=forms.TextInput(attrs={'class':'form-control','style':'width:30%;margin:10px'}))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={'class': 'form-control','style':'width:30%;margin:10px'}))
