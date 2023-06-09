"""djangocosa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from carrito.views import add_to_cart, cart, checkout, direccion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('api/', include('rest_comuna.urls')),
    path('docs/', include_docs_urls(title='Api Documentation')),
    path('carrito1/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('carrito', cart, name='carrito'),
    path('carrito/pago', checkout , name= "checkout"),
    path('direccion', direccion , name= "direccion"),
    path('order/', include('ordenes.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)