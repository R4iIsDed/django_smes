from django.urls import path
from rest_comuna.views import lista_comunas, detalle_comuna
from rest_comuna.viewslogin import login_api

urlpatterns = [
    path('lista_comunas', lista_comunas, name= "lista_comunas"),
    path('detalle_comuna', detalle_comuna, name= "detalle_comuna"),
    path('login_api', login_api, name="login_api"),
]