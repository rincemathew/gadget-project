# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
from . import models
from . import serializer
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

# Create your views here.
class ReleaseResultsView(ListAPIView):
    queryset = models.ModelName.objects.all()
    serializer_class = serializer.ModelsSerializer
    filter_backends = (DjangoFilterBackend, )
    pagination_class = ProductPagination
    # filter_fields = \
    #     {
    #         'mobileNames__brandName__brand_name': ['exact', ],
    #         'mobileNames__phone_type': ['exact'],
    #         'mobile_url_themes_name': ['exact', 'in'],
    #         'mobileGeneral__price': ['gte', 'lte', 'exact', 'in'],
    #         'mobileStorage__device_storage': ['gte', 'lte', 'exact'],
    #         'mobilePerformance__ram': ['gte', 'lte', 'exact'],
    #         'mobileGeneral__release_date': ['gte', 'lte', 'exact', 'range'],
    #         # "2020-09-30T12:00:00+05:30"
    #     }
