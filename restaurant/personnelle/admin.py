from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PosteAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('nom', 'date_add', 'date_upd', 'status')
=======
    list_display = ('id', 'nom', 'date_add', 'date_upd', 'status')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    list_filter = (
        'date_add',
        'date_upd',
        'status',
<<<<<<< HEAD

=======
        'id',
        'nom',
        'date_add',
        'date_upd',
        'status',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    )


class PersonelleAdmin(admin.ModelAdmin):

    list_display = (
<<<<<<< HEAD
=======
        'id',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
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
    list_filter = (
<<<<<<< HEAD
=======
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
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
        'date_add',
        'date_upd',
        'status',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poste, PosteAdmin)
_register(models.Personelle, PersonelleAdmin)
