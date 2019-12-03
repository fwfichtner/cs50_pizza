from django.contrib import admin
from .models import Pizza, Toppings, UserOrder, PizzaToppings


# Register your models here.
admin.site.register(Pizza)
admin.site.register(Toppings)

admin.site.register(UserOrder)
admin.site.register(PizzaToppings)
