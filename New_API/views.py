from django.shortcuts import render
from .models import Person,Address
from .serializers import PersonSerializer,AddressSerializer
from rest_framework import viewsets
# Create your views here.
class AddressRoot(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class PersonRoot(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer