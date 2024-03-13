from rest_framework import serializers
from accomodation.models import Accomodation

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accomodation
        fields='__all__'