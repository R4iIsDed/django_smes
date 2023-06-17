from django.urls import path
from rest_comuna.views import lista_comunas, detalle_comuna

urlpatterns = [
    path('lista_comunas', lista_comunas, name= "lista_comunas"),
    path('detalle_comuna', detalle_comuna, name= "detalle_comuna")
]