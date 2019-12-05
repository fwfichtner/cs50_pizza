from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def accounts(request):
    if not request.user.is_authenticated:
        return render(request, "login/login.html", {"message": None})
    context = {
        "login": request.user
    }
    return render(request, "login/accounts.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("accounts"))
    else:
        return render(request, "login/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "login/login.html", {"message": "Logged out."})