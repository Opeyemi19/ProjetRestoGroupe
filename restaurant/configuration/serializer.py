from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import *


class AboutSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class WorkingHoursSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = WorkingHours
        fields = '__all__'


class InfoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = '__all__'

class StepIndexSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = StepIndex
        fields = '__all__'


class AllFrontSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = AllFront
        fields = '__all__'


class BannerRestoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = BannerResto
        fields = '__all__'




