from django.contrib import admin
from .models import PizzaModel, Topping, PizzaSize

admin.site.register(PizzaModel)
admin.site.register(Topping)
admin.site.register(PizzaSize)
