from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TableAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'numero',
        'nombre_de_place',
        'nombre',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'numero',
        'nombre_de_place',
        'nombre',
        'date_add',
        'date_update',
        'status',
    )


class JourAdmin(admin.ModelAdmin):

    list_display = ('id', 'jour', 'date_add', 'date_update', 'status')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'jour',
        'date_add',
        'date_update',
        'status',
    )


class HeureAdmin(admin.ModelAdmin):

    list_display = ('id', 'heure', 'date_add', 'date_update', 'status')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'heure',
        'date_add',
        'date_update',
        'status',
    )


class ReservationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'email',
        'phone',
        'jour',
        'heure',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'jour',
        'heure',
        'date_add',
        'date_update',
        'status',
        'id',
        'nom',
        'email',
        'phone',
        'jour',
        'heure',
        'date_add',
        'date_update',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Table, TableAdmin)
_register(models.Jour, JourAdmin)
_register(models.Heure, HeureAdmin)
_register(models.Reservation, ReservationAdmin)
