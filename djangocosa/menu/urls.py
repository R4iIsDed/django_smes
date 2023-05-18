
from django.contrib import admin
from django.urls import path, include
from .views import login, create, index
urlpatterns = [
    path('', index, name="index "),
    path('login', login , name="login"),
    path('create', create , name="create"),
]
