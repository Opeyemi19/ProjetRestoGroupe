from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter

from .viewsets import *
from .  import views



router = DefaultRouter()
router.register('contactapi', MessageViewSet, base_name='contactapi')
router.register('newslletterapi', SouscriptionViewSet, base_name='newslletterapi')

urlpatterns = [
    path('contact/',views.contact, name="contact"),
]


urlpatterns += router.urls