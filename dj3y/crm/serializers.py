# the default import 

# my import
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# my import which may grow during adding new models
from .models import Person

# my code.


# Serializers define the API representation.
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
            'related_file',
            'related_image', 
            'parent', 
            'related_salesperson',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=Person.objects.all(),
                fields=['code', ]
            )
        ]
