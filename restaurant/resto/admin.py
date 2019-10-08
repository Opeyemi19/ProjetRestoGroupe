from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
# vim: set fileencoding=utf-8 :
=======
# Register your models here.# vim: set fileencoding=utf-8 :
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
from django.contrib import admin

from . import models


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
<<<<<<< HEAD
=======
        'id',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
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
<<<<<<< HEAD
=======
        'id',
        'nom',
        'description',
        'date_add',
        'date_update',
        'status',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    )


class MenuAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('nom', 'categorie', 'image', 'description', 'prix')
    list_filter = (
        'categorie',
=======
    list_display = ('id', 'nom', 'categorie', 'image', 'description', 'prix')
    list_filter = (
        'categorie',
        'id',
        'nom',
        'categorie',
        'image',
        'description',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
        'prix',
    )


class SpecialiteAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('id_menu', 'description')
    list_filter = ('id_menu', 'id_menu', 'description')
=======
    list_display = ('id', 'id_menu', 'description', 'image')
    list_filter = ('id_menu', 'id', 'id_menu', 'description', 'image')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Specialite, SpecialiteAdmin)
