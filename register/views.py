from django.contrib.auth import logout
from django.shortcuts import render, redirect

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
