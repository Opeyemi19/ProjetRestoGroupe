from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('teamapi', PersonelleViewSet, base_name='teamapi')


urlpatterns = [
    path('team', views.team, name="team"),
]
