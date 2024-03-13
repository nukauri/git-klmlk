from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics

from accomodation.api.serializers import AccomodationSerializer
from accomodation.models import Accomodation

class AccomodationListCreateAPIView(generics.ListCreateAPIView):
    queryset= Accomodation.objects.all()
    serializer_class=AccomodationSerializer