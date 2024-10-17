from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

from .forms import FoodForm, OrderForm
from .models import Food, Order


def home_page(request: WSGIRequest):

    if request.method == "POST":

        match request.POST.get("form-type"):
            case "add-product":
                form = FoodForm(request.POST, request.FILES)

                if form.is_valid():
                    form.save()

            case "order-product":
                form = OrderForm(request.POST)

                if form.is_valid():
                    form.save()

            case "update-product":
                instance = Food.objects.get(pk=request.POST.get("product-id"))

                files = request.FILES or [{"image": instance.image}]

                form = FoodForm(request.POST, request.FILES, instance=instance)

                if form.is_valid():
                    form.save()

                else:
                    print(form.errors)

    foods = Food.objects.all()
    form = FoodForm()
    order_form = OrderForm()

    context = {"foods": foods, "form": form, "order_form": order_form}

    return render(request, "home_page.html", context)


def orders_page(request: WSGIRequest):

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()

    orders = Order.objects.all()
    form = OrderForm()

    context = {
        "orders": orders,
        "form": form,
    }

    return render(request, "orders_page.html", context)
