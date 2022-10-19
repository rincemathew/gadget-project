from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import models
from . import serializer
from rest_framework.pagination import LimitOffsetPagination


class ProductPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
    

class EarwearListView(ListAPIView):
    queryset = models.EarModelName.objects.filter(ear_availability=True)
    serializer_class = serializer.NameSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter )
    ordering_fields = ('ear_price', 'ear_release_date')
    ordering = ('ear_release_date')
    pagination_class = ProductPagination
    filterset_fields = \
        {
            'ear_price': ['range', ],
            'ear_type': ['exact'],
            'earBrandName__ear_brand_name': ['exact',],
        }