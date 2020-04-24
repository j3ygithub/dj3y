# the default import 
from django.shortcuts import render

# my import 
from rest_framework import viewsets

# my import which may grow during adding new models
from .models import Person
from .serializers import PersonSerializer

# Create your views here.


# ViewSets define the view behavior.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer