from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/<slug:product_slug>/", views.add_product, name="add"),
    path("change/<int:product_id>/", views.change_product, name="change"),
    path("remove/<slug:product_slug>/", views.remove_product, name="remove"),
]
