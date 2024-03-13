import django_filters

from .models import Area

class AreaFilter(django_filters.FilterSet):
    class Meta:
        model=Area
        fields=['areaType']