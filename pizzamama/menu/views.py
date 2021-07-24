from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza


def index(request):
    pizzas = Pizza.objects.all()
    pizza_names_and_prices = [pizza.nom + " : " + str(pizza.prix) + "$" for pizza in pizzas]
    # return HttpResponse("Les pizzas : " + ', '.join(pizza_names_and_prices))
    return render(request, 'menu/index.html', {'pizzas': pizzas})
