from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('menu/', views.Menu , name="menu"),
    path('about/', views.About, name="about"),
    path('special/', views.specialite, name="special"),
]