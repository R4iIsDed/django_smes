
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from menu import views
from .views import agregar_producto, banadmin, borrarcuenta, Cactus, create_html, Carrito, Categorias, changeforgoh, chNGE, compra_cactus1, compra_cactus2, compra_cactus3, compra_cactus4, compra_cactus5, compra_cactus6, Compra_fertilizante1, Compra_fertilizante2, Compra_fertilizante3, Compra_fertilizante4, Compra_fertilizante5, Compra_fertilizante6, Compra_maceta1, Compra_maceta2, Compra_maceta3, Compra_maceta4, Compra_maceta5, Compra_maceta6, Compra_Pago, Compra_pesticida1 ,Compra_pesticida2, Compra_pesticida3, compra_planta1, Compra_planta2, Compra_planta3, Compra_planta4, Compra_planta5, Compra_planta6, Contacto, editar_producto, eliminar_producto, Fertilizante, Flores, index, login, Maceteros, oferta1, oferta2, oferta3, oferta4, oferta5, oferta6, ofertas, Perfil_administrador, Pesticidas, profile, Cfertilizante
from django.urls.conf import re_path
from .views import create_admin
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', index , name="index"),
    path('login', login , name="login"),
    path('create_html', create_html , name="create_html"),
    path('agregar_producto', agregar_producto, name="agregar_producto"),
    path('banadmin', banadmin, name="banadmin"),
    path('borrarcuenta', borrarcuenta, name="borrarcuenta"),
    path('Cactus', Cactus, name="Cactus"),
    path('Carrito', Carrito, name="Carrito"),
    path('Categorias', Categorias, name="Categorias"),
    path('changeforgoh', changeforgoh, name="changeforgoh"),
    path('chNGE', chNGE, name="chNGE"),
    path('compra_cactus1', compra_cactus1, name="compra_cactus1"),
    path('compra_cactus2', compra_cactus2, name="compra_cactus2"),
    path('compra_cactus3', compra_cactus3, name="compra_cactus3"),
    path('compra_cactus4', compra_cactus4, name="compra_cactus4"),
    path('compra_cactus5', compra_cactus5, name="compra_cactus5"),
    path('compra_cactus6', compra_cactus6, name="compra_cactus6"),
    path('Compra_fertilizante1', Compra_fertilizante1, name="Compra_fertilizante1"),
    path('Compra_fertilizante2', Compra_fertilizante2, name="Compra_fertilizante2"),
    path('Compra_fertilizante3', Compra_fertilizante3, name="Compra_fertilizante3"),
    path('Compra_fertilizante4', Compra_fertilizante4, name="Compra_fertilizante4"),
    path('Compra_fertilizante5', Compra_fertilizante5, name="Compra_fertilizante5"),
    path('Compra_fertilizante6', Compra_fertilizante6, name="Compra_fertilizante6"),
    path('Compra_maceta1', Compra_maceta1, name="Compra_maceta1"),
    path('Compra_maceta2', Compra_maceta2, name="Compra_maceta2"),
    path('Compra_maceta3', Compra_maceta3, name="Compra_maceta3"),
    path('Compra_maceta4', Compra_maceta4, name="Compra_maceta4"),
    path('Compra_maceta5', Compra_maceta5, name="Compra_maceta5"),
    path('Compra_maceta6', Compra_maceta6, name="Compra_maceta6"),
    path('Compra_Pago', Compra_Pago, name="Compra_Pago"),
    path('Compra_pesticida1', Compra_pesticida1, name="Compra_pesticida1"),
    path('Compra_pesticida2', Compra_pesticida2, name="Compra_pesticida2"),
    path('Compra_pesticida3', Compra_pesticida3, name="Compra_pesticida3"),
    path('compra_planta1', compra_planta1, name="compra_planta1"),
    path('Compra_planta2', Compra_planta2, name="Compra_planta2"),
    path('Compra_planta3', Compra_planta3, name="Compra_planta3"),
    path('Compra_planta4', Compra_planta4, name="Compra_planta4"),
    path('Compra_planta5', Compra_planta5, name="Compra_planta5"),
    path('Compra_planta6', Compra_planta6, name="Compra_planta6"),
    path('Contacto', Contacto, name="Contacto"),
    path('editar_producto', editar_producto, name="editar_producto"),
    path('eliminar_producto', eliminar_producto, name="eliminar_producto"),
    path('Fertilizante', Fertilizante, name="Fertilizante"),
    path('Flores', Flores, name="Flores"),
    path('Maceteros', Maceteros, name="Maceteros"),
    path('oferta1', oferta1, name="oferta1"),
    path('oferta2', oferta2, name="oferta2"),
    path('oferta3', oferta3, name="oferta3"),
    path('oferta4', oferta4, name="oferta4"),
    path('oferta5', oferta5, name="oferta5"),
    path('oferta6', oferta6, name="oferta6"),
    path('ofertas', ofertas, name="ofertas"),
    path('Perfil_administrador', Perfil_administrador, name="Perfil_administrador"),
    path('Pesticidas', Pesticidas, name="Pesticidas"),
    path('profile', profile, name="profile"),
    path('producto/<int:id>/', Cfertilizante, name='Cfertilizante'),
    path('create_admin', create_admin, name="create_admin")

]

urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$',serve,{
        'document_root':settings.MEDIA_ROOT,
    })

]