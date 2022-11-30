"""Biyan_Huang URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.hello, name='home'),
    path('now/', views.current, name='time'),
    path('add_movie/', views.addMovie, name='add'),
    path('edit_movie/<str:id>', views.editMovie, name='edit'),
    path('delete_movie/<str:id>', views.deleteMovie, name='delete'),
    path('<str:id>/', views.displayById, name="identifier"),
    path('get_xkcd/', views.comic, name='xkcd'),
    path('get_dog/', views.dog, name='dog'),
    path('get_code/', views.code, name='QR'),


]
