from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Pizza, Toppings


# Create your views here.
def index(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)


def order(request):  # TODO add a user ID
    try:
        pizza_id = int(request.POST["pizza"])
        pizza = Pizza.objects.get(pk=pizza_id)
        # TODO add user ID
    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "Pizza does not exist."})

    # TODO add Pizza to user ID
    return HttpResponseRedirect(HttpResponse("Thanks for ordering. We will finish this website and then eat the Pizza "
                                             "ourselves."))
