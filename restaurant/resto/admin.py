from django.contrib import admin
from django.utils.safestring import mark_safe
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

    )

class MenuJourAdmin(admin.ModelAdmin):
    
    list_display = (
        'id_menu',
        'jour',
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

    list_display = ('nom', 'categorie','menujour', 'afficheImage', 'description', 'date_add', 'prix')
    list_filter = (
        'categorie',
    )

    def __str__(self):
        """Unicode representation of Menu."""
        return self.nom
    
    def afficheImage(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))

class SpecialiteAdmin(admin.ModelAdmin):

    list_display = ('id', 'id_menu', 'description', 'date_add', 'image')
    list_filter = ('id_menu', )


def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.MenuJour, MenuJourAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Menu, MenuAdmin)
_register(models.Specialite, SpecialiteAdmin)
