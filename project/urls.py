from django.urls import path
from .views import home_page, orders_page


urlpatterns = [
    path("", home_page, name="home_page"),
    path("orders/", orders_page, name="orders_page"),
]
