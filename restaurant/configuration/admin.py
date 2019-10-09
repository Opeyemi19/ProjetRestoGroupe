from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class BannerRestoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'image_banner',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
    )



class AllFrontAdmin(admin.ModelAdmin):

    list_display = (
        'logo',
        'headerText',
        'movieInto',
        'footText',
        'newsletterText',
        'imageTesti',
        'imageReservations',
        'status',
    )
    list_filter = (
        'status',
        'id',
    )


class StepIndexAdmin(admin.ModelAdmin):
    list_display = ('icon', 'text', 'status')
    list_filter = ('status',)



class InfoAdmin(admin.ModelAdmin):

    list_display = ('fbLink', 'twLink', 'instaLink', 'phone')


class WorkingHoursAdmin(admin.ModelAdmin):
    list_display = ('day', 'openHours', 'closeHours', 'status')
    list_filter = (
        'status',
        'day',
    )

class AboutAdmin(admin.ModelAdmin):

    list_display = ('headerText', 'description', 'image')
    list_filter = ('headerText',)



def _register(model, admin_class):
    admin.site.register(model, admin_class)



_register(models.BannerResto, BannerRestoAdmin)
_register(models.AllFront, AllFrontAdmin)
_register(models.StepIndex, StepIndexAdmin)
_register(models.Info, InfoAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
_register(models.About, AboutAdmin)
