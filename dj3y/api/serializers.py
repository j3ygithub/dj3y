# the default import 

# my import
from rest_framework import serializers

# my import which may grow during adding new models
from crm.models import Person
from crm.models import Device

# my code


class PersonSerializer(serializers.ModelSerializer):
    
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
            'age',
            'parent',
            'related_salesperson',
        )
        extra_kwargs = {
            'url': {'view_name': 'crm:person-detail'}
        }


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = (
            'url',
            'id',
            'code',
            'name',
            'power_state',
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