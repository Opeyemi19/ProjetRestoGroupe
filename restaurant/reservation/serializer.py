from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class ReservationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # jour = serializers.SlugRelatedField(many=False, read_only=True, slug_field='jour')
    # heure = serializers.SlugRelatedField(many=False, read_only=True, slug_field='heure')
    # nbre_reservation = serializers.SlugRelatedField(many=False, read_only=True, slug_field='personne')

    class Meta:
        model = Reservation
        fields = '__all__'



class TableMessageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # person_reserver = ReservationSerializer(many=True,  read_only=True, required=False)

    jour_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='jour')
    heure_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='heure')
    person_id = serializers.SlugRelatedField(many=False, read_only=True, slug_field='personne')

    class Meta:
        model = TableMessage
        fields = '__all__'




class PersonSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # person_reserver = ReservationSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = Person
        fields = '__all__'


class HeureSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # heure_reserver = ReservationSerializer(many=True,  read_only=True, required=False)

    class Meta:
        model = Heure
        fields = '__all__'


class JourSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # Jour_reserver = ReservationSerializer(many=True,  read_only=True, required=False)


    class Meta:
        model = Jour
        fields = '__all__'


class TableSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Table
        fields = '__all__'