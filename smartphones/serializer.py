from rest_framework import serializers
from . import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BrandName
        fields = '__all__'


class NameSerializer(serializers.ModelSerializer):
    brandName = BrandSerializer(many=False)

    class Meta:
        model = models.MobileName
        fields = ['mobile_name', 'mobile_name_url', 'mobile_image', 'phone_type', 'brandName',]


class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileGeneral
        fields = '__all__'


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobilePerformance
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileStorage
        fields = '__all__'


class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileCamera
        fields = '__all__'


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileBattery
        fields = '__all__'


class DisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileDisplay
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MobileSensor
        fields = '__all__'


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OtherFeature
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    mobileNames = NameSerializer(many=False)
    mobileGeneral = GeneralSerializer(many=False)
    mobilePerformance = PerformanceSerializer(many=False)
    mobileStorage = StorageSerializer(many=False)
    mobileCamera = CameraSerializer(many=False)
    mobileBattery = BatterySerializer(many=False)
    mobileDisplay = DisplaySerializer(many=False)
    # mobileConnectivity = MobileConnectivitySerializer(many=False)
    mobileSensor = SensorSerializer(many=False)
    otherFeature = FeatureSerializer(many=False)
    # variant_Color = VariantColorSerializer(many=True)
    # variant_Image = VariantImageSerializer(many=True)

    class Meta:
        model = models.MobileVariant
        fields = ['mobile_variants', 'mobile_variants_url', 'mobile_url_themes_name', 'mobileNames', 'mobileGeneral', 'mobilePerformance', 
        'mobileStorage', 'mobileCamera', 'mobileBattery', 'mobileDisplay', 'mobileSensor', 'otherFeature']