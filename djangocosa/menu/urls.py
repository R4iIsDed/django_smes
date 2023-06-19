
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from menu import views
from .views import agregar_producto, banadmin, borrarcuenta, Cactus, create_html, Carrito, Categorias, changeforgoh, chNGE, compra_cactus1, compra_cactus2, compra_cactus3, compra_cactus4, compra_cactus5, compra_cactus6, Compra_fertilizante1, Compra_fertilizante2, Compra_fertilizante3, Compra_fertilizante4, Compra_fertilizante5, Compra_fertilizante6, Compra_maceta1, Compra_maceta2, Compra_maceta3, Compra_maceta4, Compra_maceta5, Compra_maceta6, Compra_Pago, Compra_pesticida1 ,Compra_pesticida2, Compra_pesticida3, compra_planta1, Compra_planta2, Compra_planta3, Compra_planta4, Compra_planta5, Compra_planta6, Contacto, editar_producto, eliminar_producto, Fertilizante, Flores, index, login2, Maceteros, oferta1, oferta2, oferta3, oferta4, oferta5, oferta6, ofertas, Perfil_administrador, Pesticidas, profile, Cfertilizante, editarProducto, ver_usuario
from django.urls.conf import re_path
from .views import create_admin, logout_view
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
    path('chNGE/<int:id>', chNGE, name="chNGE"),
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
    path('ver_usuario', ver_usuario, name="ver_usuario")
]

urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })

]