from django.contrib import admin
from django.urls import path
from shop_app import views

urlpatterns = [
    path('', views.index),
    path('list', views.list),
    path('form', views.form),
]