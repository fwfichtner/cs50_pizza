from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Toppings, UserOrder, PizzaToppings


# Create your views here.
def index(request):
    context = {
        "pizzas": Pizza.objects.all(),
        "toppings": Toppings.objects.all()
    }
    return render(request, "orders/index.html", context)


def order(request):
    try:
        pizza_id = int(request.POST["pizza"])
        pizza = Pizza.objects.get(pk=pizza_id)
        u = UserOrder(user=request.user, pizza=pizza, numberToppings=pizza.size)  # add Pizza to order of user
        u.save()
    except KeyError:
        return render(request, "orders/error.html", {"message": "No selection."})
    except Pizza.DoesNotExist:
        return render(request, "orders/error.html", {"message": "Pizza does not exist."})

    if f"{u.numberToppings}" == "0":
        return HttpResponse(f"Thanks {request.user} for ordering a {pizza}. "
                            f"We will finish this website and then eat the Pizza ourselves.")
    else:
        return finalize(request, u.pk)


def finalize(request, order_number):
    u = UserOrder.objects.get(pk=order_number)
    context = {
        "userorder": u,
        "toppings": Toppings.objects.all()
    }
    try:
        topping_id = int(request.POST["topping"])
        topping = Toppings.objects.get(pk=topping_id)
        p = PizzaToppings(order=u, usedTopping=topping)
        p.save()
        if str(len(PizzaToppings.objects.filter(order=u))) == f"{u.pizza.size}":
            return HttpResponse(f"Thanks {request.user} for ordering a {u.pizza}. "
                                f"We will finish this website and then eat the Pizza ourselves.")
        else:
            return render(request, "orders/finalize.html", context)
    except KeyError:  # no topping yet
        return render(request, "orders/finalize.html", context)

