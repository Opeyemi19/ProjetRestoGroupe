from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import *
from . import views


router = DefaultRouter()
router.register('categorieapi', CategorieViewSet, base_name='categorieapi')
router.register('menuapi', MenuViewSet, base_name='menuapi')
router.register('specialapi', SpecialiteViewSet, base_name='specialapi')




urlpatterns = [
    path('', views.home , name="home"),
    path('menu/', views.Menu , name="menu"),
    path('about/', views.About, name="about"),
    path('special/', views.specialite, name="special"),
]


urlpatterns += router.urls