from django.contrib import admin

# Register your models here.# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'description',
        'date_add',
        'date_update',
        'status',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'nom',
        'description',
        'date_add',
        'date_update',
        'status',
    )


class MenuAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'categorie', 'image', 'description', 'prix')
    list_filter = (
        'categorie',
        'id',
        'nom',
        'categorie',
        'image',
        'description',
        'prix',
    )


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'id_menu', 'description', 'image')
    list_filter = ('id_menu', 'id', 'id_menu', 'description', 'image')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Specialite, SpecialiteAdmin)
