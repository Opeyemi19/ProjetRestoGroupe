from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class ReservationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class HeureSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Heure
        fields = '__all__'


class JourSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Jour
        fields = '__all__'


class TableSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'