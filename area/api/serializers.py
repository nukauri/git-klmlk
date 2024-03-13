from rest_framework import serializers
from area.models import Address,Area




class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'



class AreaSerializer(serializers.ModelSerializer):

    addresses = AddressSerializer(many=True,read_only=True)
    class Meta:
        model=Area
        fields=['name','areaType','addresses']