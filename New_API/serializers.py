from rest_framework import serializers
from .models import Person
from .models import Address

class PersonSerializer(serializers.ModelSerializer):
    pin=serializers.IntegerField(source='address.pin',read_only=True)
    state = serializers.CharField(source='address.state',read_only=True)
    class Meta:
        model=Person
        fields=['name','age','sex','color','address','pin','state']
class AddressSerializer(serializers.ModelSerializer):
    person=PersonSerializer(read_only=True,many=True)
    class Meta:
        model=Address
        fields='__all__'

