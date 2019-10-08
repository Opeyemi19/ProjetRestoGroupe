from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('teamapi', PersonelleViewSet, base_name='teamapi')


urlpatterns = [
<<<<<<< HEAD
    path('team', views.team, name="team"),
]
=======
    path('team/', views.team, name="team"),
]


urlpatterns += router.urls
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
