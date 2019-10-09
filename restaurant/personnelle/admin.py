from django.contrib import admin
from django.utils.safestring import mark_safe
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
    )


class PersonelleAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'afficheImage',
        'date_add',
        'date_upd',
        'status',
    )
    list_filter = (
        'poste',
        'date_add',
        'date_upd',
        'status',
    )
    def afficheImage(self, obj):
        return mark_safe('<img src = " {url} " width = " 100px " heigth = " 50px " />'.format(url=obj.image.url))

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poste, PosteAdmin)
_register(models.Personelle, PersonelleAdmin)
