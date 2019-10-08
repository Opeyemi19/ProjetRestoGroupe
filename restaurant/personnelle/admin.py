from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PosteAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'date_add', 'date_upd', 'status')
    list_filter = (
        'date_add',
        'date_upd',
        'status',
        'id',
        'nom',
        'date_add',
        'date_upd',
        'status',
    )


class PersonelleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'image',
        'poste',
        'twitter',
        'facebook',
        'google',
        'instagram',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'poste',
        'date_add',
        'date_upd',
        'status',
        'id',
        'nom',
        'poste',
        'twitter',
        'facebook',
        'google',
        'instagram',
        'date_add',
        'date_upd',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poste, PosteAdmin)
_register(models.Personelle, PersonelleAdmin)
