from rest_framework import status
from rest_framework.response import Response

from area.models import Address,Area
from area.api.serializers import AddressSerializer,AreaSerializer
from rest_framework.generics import ListAPIView

from django_filters.rest_framework import DjangoFilterBackend
from area.filters import AreaFilter

class AreaListAPIView(ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AreaFilter


class AddressListAPIView(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer