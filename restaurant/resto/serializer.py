from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class SpecialiteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Specialite
        fields = '__all__'


class MenuSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    menu_speciale = SpecialiteSerializer(many=True, read_only=True, required=False)

    # categelement = CategorieSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'nom',
            'prix',
            'image',
            'description',
            'menu_speciale',
        ]


class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    Catégorie_menu = MenuSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Categorie
        fields = '__all__'