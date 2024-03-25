from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class login(forms.Form) :
    username = forms.CharField(max_length=50,label='nom utilisateur')
    password = forms.CharField(max_length=50,widget=forms.PasswordInput,label='mot de passe')

class Inscription(UserCreationForm) :
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('user_photo','username','email','first_name')
        


