from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("", views.index, name="index"), #страница аккаунта
    path("login/", views.login, name="login"), #вход в аккаунт
    path("register/", views.register, name="register"), #создание аккаунта
    path("logout/", views.logout, name="logout"),
]
