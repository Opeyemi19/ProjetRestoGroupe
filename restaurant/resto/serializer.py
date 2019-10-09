from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *

class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__'
        
class MenuSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    # Catégorie_menu = CategorieSerializer(many=True, read_only=True, required=False,)
    # categelement = CategorieSerializer(read_only=True)

    categorie = CategorieSerializer(many=False, read_only=True)

    class Meta:
        model = Menu
        fields = [
            'nom',
            'prix',
            'image',
            'description',
            'categorie'
        ]
        
class SpecialiteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    myvar = MenuSerializer(many=False, read_only=True)

    class Meta:
        model = Specialite
        fields = '__all__'



