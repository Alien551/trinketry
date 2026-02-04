from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path("", views.index, name="shop"),
    path("product/<int:product_id>/", views.product, name="product")
]
