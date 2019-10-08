from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class AllFrontAdmin(admin.ModelAdmin):

    list_display = (
<<<<<<< HEAD
=======
        'id',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
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
<<<<<<< HEAD
        
=======
        'id',
        'logo',
        'headerText',
        'movieInto',
        'footText',
        'newsletterText',
        'imageTesti',
        'imageReservations',
        'status',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    )


class StepIndexAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('icon', 'text', 'status')
    list_filter = ('status',)
=======
    list_display = ('id', 'icon', 'text', 'status')
    list_filter = ('status', 'id', 'icon', 'text', 'status')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2


class InfoAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('fbLink', 'twLink', 'instaLink', 'phone')
    
=======
    list_display = ('id', 'fbLink', 'twLink', 'instaLink', 'phone')
    list_filter = ('id', 'fbLink', 'twLink', 'instaLink', 'phone')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2


class WorkingHoursAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('day', 'openHours', 'closeHours', 'status')
    list_filter = (
        'status',
        'day',
=======
    list_display = ('id', 'day', 'openHours', 'closeHours', 'status')
    list_filter = (
        'status',
        'id',
        'day',
        'openHours',
        'closeHours',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
        'status',
    )


class AboutAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('headerText', 'description', 'image')
    list_filter = ('headerText',)
=======
    list_display = ('id', 'headerText', 'description', 'image')
    list_filter = ('id', 'headerText', 'description', 'image')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.AllFront, AllFrontAdmin)
_register(models.StepIndex, StepIndexAdmin)
_register(models.Info, InfoAdmin)
_register(models.WorkingHours, WorkingHoursAdmin)
_register(models.About, AboutAdmin)
