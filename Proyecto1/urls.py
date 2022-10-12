"""Proyecto1 URL Configuration

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
from django.urls import path
from Proyecto1.views import saludo, despedida, dame_fecha, muestra_edad, calcula_edad, saludo_plantilla, saludo_plantilla_variables, saludo_plantilla_clase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('nosvamos/', despedida),
    path('fecha/', dame_fecha),
    # necesitamos que pase el parámetro como número, si no, lo pasaría como texto
    path('edad/<int:any>', muestra_edad),
    # pasamos 2 parámetros
    path('edades/<int:edad>/<int:any>', calcula_edad),
    # usamos plantilla
    path('plantilla/', saludo_plantilla),
    # usamos plantilla con variables
    path('plantilla_variables/', saludo_plantilla_variables),
    path('plantilla_clase/', saludo_plantilla_clase),

      
]
