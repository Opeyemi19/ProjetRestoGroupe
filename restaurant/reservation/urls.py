from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('jourapi', JourViewSet, base_name='jourapi')
router.register('heureapi', HeureViewSet, base_name='heureapi')
router.register('personapi', PersonViewSet, base_name='personapi')
router.register('messageresvationapi', TableMessageViewSet, base_name='messageresvationapi')
router.register('reservationapi', ReservationViewSet, base_name='reservationapi')


urlpatterns = [
   path('reservation/', views.reservation, name="reservation"),
]


urlpatterns += router.urls