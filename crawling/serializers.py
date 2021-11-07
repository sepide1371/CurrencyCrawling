from rest_framework import serializers
from .models import CurrentPrice, UsdEuroRatio


class CurrentPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentPrice
        fields = '__all__'


class UsdEuroRatioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsdEuroRatio
        fields = '__all__'

