from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *

class PersonelleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Personelle
        fields = '__all__'


class PosteSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    poste_personnelle = PersonelleSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Poste
        fields = '__all__'  