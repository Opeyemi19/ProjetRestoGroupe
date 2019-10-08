from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class MessageAdmin(admin.ModelAdmin):

    list_display = (
<<<<<<< HEAD
=======
        'id',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
        'nom',
        'sujet',
        'email',
        'message',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
<<<<<<< HEAD

=======
        'id',
        'nom',
        'sujet',
        'email',
        'message',
        'status',
        'date_add',
        'date_upd',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    )


class SouscriptionAdmin(admin.ModelAdmin):

<<<<<<< HEAD
    list_display = ('email', 'status', 'date_add', 'date_upd')
=======
    list_display = ('id', 'email', 'status', 'date_add', 'date_upd')
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    list_filter = (
        'status',
        'date_add',
        'date_upd',
<<<<<<< HEAD
=======
        'id',
        'email',
        'status',
        'date_add',
        'date_upd',
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Message, MessageAdmin)
<<<<<<< HEAD
_register(models.Souscription, SouscriptionAdmin)
=======
_register(models.Souscription, SouscriptionAdmin)
>>>>>>> a404c4bcfc81a1442b85037e63c5076e153d29e2
