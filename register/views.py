from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm

# Create your views here.



def logout_view(request):
    logout(request)
    return render(request, "register/signup.html", {"message": "Logged out."})


def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/login')
    else:
         form = RegisterForm()
    return render(request, "register/signup.html", {"form": form})