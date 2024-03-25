from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django import forms
from authentification.models import User_connect
# Create your views here.

@login_required
def homepage(requests) :
    user_connect = User_connect.objects.all()
    return render(requests,'application/home.html',{"user_connect" : user_connect})
@login_required
def about(requests):
    return render(requests,'application/about.html')