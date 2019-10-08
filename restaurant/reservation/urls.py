from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('reservationapi', ReservationViewSet, base_name='reservationapi')


urlpatterns = [
   path('reservation/', views.reservation, name="reservation"),
]


urlpatterns += router.urls