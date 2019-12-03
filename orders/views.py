from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Toppings


# Create your views here.
def index(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)


def order(request):
    return HttpResponse("Project 3: TODO")