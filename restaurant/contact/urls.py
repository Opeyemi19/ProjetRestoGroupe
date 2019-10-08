from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views


router = DefaultRouter()
router.register('contactapi', MessageViewSet, base_name='contactapi')

urlpatterns = [
    path('contact/',views.contact, name="contact"),
]


urlpatterns += router.urls