
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from menu import views
from .views import agregar_producto, banadmin, borrarcuenta, Cactus, create_html, Carrito, Categorias, changeforgoh, chNGE, Compra_Pago, Contacto, editar_producto, eliminar_producto, Fertilizante, Flores, index, login2, Maceteros, ofertas, Perfil_administrador, Pesticidas, profile, Cfertilizante, editarProducto, ver_usuario
from django.urls.conf import re_path
from .views import create_admin, logout_view, modi
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', index , name="index"),
    path('login', login2 , name="login"),
    path('create_html', create_html , name="create_html"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('banadmin', banadmin, name="banadmin"),
    path('borrarcuenta', borrarcuenta, name="borrarcuenta"),
    path('Cactus', Cactus, name="Cactus"),
    path('Carrito', Carrito, name="Carrito"),
    path('Categorias', Categorias, name="Categorias"),
    path('changeforgoh', changeforgoh, name="changeforgoh"),
    path('chNGE', chNGE, name="chNGE"),
    path('Compra_Pago', Compra_Pago, name="Compra_Pago"),
    path('Contacto', Contacto, name="Contacto"),
    path('editar_producto', editar_producto, name="editar_producto"),
    path('eliminar_producto', eliminar_producto, name="eliminar_producto"),
    path('Fertilizante', Fertilizante, name="Fertilizante"),
    path('Flores', Flores, name="Flores"),
    path('Maceteros', Maceteros, name="Maceteros"),
    path('ofertas', ofertas, name="ofertas"),
    path('Perfil_administrador', Perfil_administrador, name="Perfil_administrador"),
    path('Pesticidas', Pesticidas, name="Pesticidas"),
    path('profile', profile, name="profile"),
    path('Cfertilizante/<int:id>', Cfertilizante, name="Cfertilizante"),
    path('create_admin', create_admin, name="create_admin"),
    path('editarProducto', editarProducto, name="editarProducto"),
    path('cerrarsion', logout_view, name="logout"),
    path('ver_usuario', ver_usuario, name="ver_usuario"),
    path('modificar', modi, name="modi")
]

urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })

]