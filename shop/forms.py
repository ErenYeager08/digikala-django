from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={ 'class': 'form-control', 'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'فامیلیتو بزن'})) 
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیلت'}), max_length=50, required=False)
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control', 'placeholder': 'رمزت وارد کن'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput({
        'class': 'form-control', 'placeholder': 'رمزت وارد کن'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']