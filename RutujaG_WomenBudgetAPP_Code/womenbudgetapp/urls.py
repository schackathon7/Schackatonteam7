from django.urls import path, include
from . import views
from .views import *



urlpatterns = [
    path('', views.IndexView, name="index"),
    path('register', views.RegisterPage, name="register"),
    path('login', views.login, name="login"),
    path('update', UpdateView, name="update"),
    path('AddWalletAmount', AddWalletAmount, name="AddWalletAmount"),
    path('CalculateSaving',CalculateSaving, name="CalculateSaving"),
    path('FetchAllGoals', FetchAllGoals, name="FetchAllGoals"),

]

