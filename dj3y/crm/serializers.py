# the default import 

# my import
from rest_framework import serializers

# my import which may grow during adding new models
from .models import Person
from .models import Device

# my code


class PersonSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'url',
            'id',
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


class DeviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Device
        fields = (
            'url',
            'id',
            'code', 
            'name', 
            'power_on', 
            'os', 
            'cpu', 
            'ram',
            'registration_time',
            'expiration_time',
            'vmware_tool_state',
            'remark', 
            'parent',
            'customer',
        )