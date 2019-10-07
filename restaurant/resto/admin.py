from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
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
    )


class MenuAdmin(admin.ModelAdmin):

    list_display = ('nom', 'categorie', 'image', 'description', 'prix')
    list_filter = (
        'categorie',
        'prix',
    )


class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id_menu', 'description')
    list_filter = ('id_menu', 'id_menu', 'description')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Specialite, SpecialiteAdmin)
