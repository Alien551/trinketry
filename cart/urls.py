from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_product, name="add"),
    path("change/", views.change_product, name="change"),
    path("remove/", views.remove_product, name="remove"),
]
