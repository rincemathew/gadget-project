from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandName
        fields = ['brand_name']


class ModelsSerializer(serializers.ModelSerializer):
    brandName = BrandSerializer(many=False)

    class Meta:
        model = models.ModelName
        fields = ['model_name', 'model_name', 'release_date', 'mobile_image', 'phone_type', 'description', 'brandName',]