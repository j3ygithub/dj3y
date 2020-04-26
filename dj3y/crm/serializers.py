# the default import 

# my import
from rest_framework import serializers

# my import which may grow during adding new models
from .models import Person

# my code


# serializers define the API representation.
class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'code', 
            'name', 
            'tax_id', 
            'phone_number', 
            'address', 
            'registration_time',
            'expiration_time', 
            'remark', 
            'parent', 
            'related_salesperson',
        )
