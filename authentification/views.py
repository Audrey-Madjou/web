from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from . import forms
from django.conf import settings
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def connection (requests):
    user_connect = forms.login()#intanciation du formulaire
    message = ""
    if (requests.method == 'POST') :
        form = forms.login(requests.POST)
        if(form.is_valid()) :
            #on recupere les valeurs du usermane et  password et on sauvegarde dans la variable user
            user = authenticate(username = form.cleaned_data ['username'],
                                password = form.cleaned_data['password'])
            if(user is not None) :
                login(requests,user)
               # redirect("Home")
                message = f"valider {user.username}"
                return render(requests,"application/home.html")
            else :
                message = "Identiant invalide"
    return render(requests,"authentification/connection.html",{"message" : message,"user_connect" : user_connect})


def log_out(requests) :
    logout(requests)
    return redirect("connection")

def inscription(requests) :
    user_inscrip = forms.Inscription()
    if (requests.method == 'POST') :
        user_inscrip = forms.Inscription(requests.POST,requests.FILES)
        if(user_inscrip.is_valid()) :
            user = user_inscrip.save()
            login(requests,user)
            return redirect(settings.LOGIN_URL)#voir settings,redirection vers la page qui est valeur de login_url
    return render(requests,"authentification/inscription.html",{"user_inscrip" : user_inscrip})

