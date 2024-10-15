from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import model_to_dict

from .forms import FoodForm, OrderForm
from .models import Food, Order


def home_page(request: WSGIRequest):

    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)

        if form.is_valid():
            form.create()

    foods = Food.objects.all()
    form = FoodForm()

    context = {
        "foods": foods,
        "form": form,
    }

    return render(request, "home_page.html", context)


def orders_page(request: WSGIRequest):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.create()

    orders = Order.objects.all()
    form = OrderForm()

    context = {
        "orders": orders,
        "form": form,
    }

    return render(request, "orders_page.html", context)

