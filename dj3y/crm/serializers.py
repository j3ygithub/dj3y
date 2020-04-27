# the default import 

# my import
from rest_framework import serializers
import uuid
from django.core.exceptions import ValidationError

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

    def create(self, validated_data):

        code = validated_data['code']
        if code == 'auto':
            code = f'{Person._meta.verbose_name[0:3]}. {uuid.uuid4().hex[:6]}'
        person = Person(
            code=code,
        )
        person.save()
        return person


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