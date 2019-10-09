from rest_framework.routers import DefaultRouter

from .viewsets import *


router = DefaultRouter()
router.register('bannerapi', BannerRestoViewSet, base_name='bannerapi')
router.register('allfront', AllFrontViewSet, base_name='allfront')
router.register('stepindex', StepIndexViewSet, base_name='stepindex')
router.register('info', InfoViewSet, base_name='info')
router.register('works', WorkingHoursViewSet, base_name='works')
router.register('about', AboutViewSet, base_name='about')


urlpatterns = [
    
]


urlpatterns += router.urls