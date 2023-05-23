import django_filters
from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at_from = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_to = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    updated_at_from = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='gte')
    updated_at_to = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='lte')
    status = django_filters.ChoiceFilter(choices=Advertisement.status)
    author_username = django_filters.CharFilter(field_name='author__username', lookup_expr='iexact')

    class Meta:
        model = Advertisement
        fields = ['created_at_from', 'created_at_to', 'updated_at_from', 'updated_at_to', 'status', 'author_username']