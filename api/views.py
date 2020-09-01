# the default import 
from django.shortcuts import render

# my import 
from rest_framework import viewsets

# my import which may grow during adding new models
from crm.models import Person
from .serializers import PersonSerializer
from crm.models import Device
from .serializers import DeviceSerializer

# Create your views here.


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer