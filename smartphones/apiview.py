from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import models
from . import serializer
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 8
    max_limit = 100
    

class MobileListView(ListAPIView):
    queryset = models.MobileVariant.objects.filter(mobileGeneral__is_available=True)
    serializer_class = serializer.VariantSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('mobileGeneral__price', 'mobileGeneral__release_date')
    ordering = ('mobileGeneral__release_date')
    pagination_class = ProductPagination
    filterset_fields = \
        {
            'mobileGeneral__price': ['range',],
            'mobileNames__brandName__brand_name': ['in', 'exact',],
            'mobilePerformance__ram': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileStorage__device_storage': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileBattery__battery_capacity': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileDisplay__screen_size': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileCamera__primary_camera': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileCamera__secondary_camera': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobilePerformance__processor_company': ['in', 'exact'],
            'mobileDisplay__resolution_type': ['in', 'exact'],
            'mobileGeneral__os': ['in', 'exact'],
            'mobilePerformance__clock_speed': ['in', 'exact', 'gte', 'lte', 'range'],
            'mobileGeneral__os_version': ['in', 'exact'],
            # "2020-09-30T12:00:00+05:30"
        }