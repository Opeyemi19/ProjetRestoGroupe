from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AllFrontAdmin(admin.ModelAdmin):

    list_display = (
        'id',
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
        'logo',
        'headerText',
        'movieInto',
        'footText',
        'newsletterText',
        'imageTesti',
        'imageReservations',
        'status',
    )


class StepIndexAdmin(admin.ModelAdmin):

    list_display = ('id', 'icon', 'text', 'status')
    list_filter = ('status', 'id', 'icon', 'text', 'status')


class InfoAdmin(admin.ModelAdmin):

    list_display = ('id', 'fbLink', 'twLink', 'instaLink', 'phone')
    list_filter = ('id', 'fbLink', 'twLink', 'instaLink', 'phone')


class WorkingHoursAdmin(admin.ModelAdmin):

    list_display = ('id', 'day', 'openHours', 'closeHours', 'status')
    list_filter = (
        'status',
        'id',
        'day',
        'openHours',
        'closeHours',
        'status',
    )


class AboutAdmin(admin.ModelAdmin):

    list_display = ('id', 'headerText', 'description', 'image')
    list_filter = ('id', 'headerText', 'description', 'image')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AllFront, AllFrontAdmin)
_register(models.StepIndex, StepIndexAdmin)
_register(models.Info, InfoAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
_register(models.About, AboutAdmin)
