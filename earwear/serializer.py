from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EarBrandName
        fields = '__all__'


class NameSerializer(serializers.ModelSerializer):
    earBrandName = BrandSerializer(many=False)

    class Meta:
        model = models.EarModelName
        fields = '__all__'