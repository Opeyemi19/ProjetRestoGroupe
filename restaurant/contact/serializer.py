from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class SouscriptionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Souscription
        fields = '__all__'


class MessageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'