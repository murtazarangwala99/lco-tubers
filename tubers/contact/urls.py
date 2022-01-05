from django.urls import path

from . import views

urlpatterns = [
    path('header', views.detail,name="detail"),
]