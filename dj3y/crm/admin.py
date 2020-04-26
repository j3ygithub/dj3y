# the default import
from django.contrib import admin

# my import


# my import which may grow during adding new models
from .models import Person
from .models import Device

# Register your models here.

admin.site.register(Person)
admin.site.register(Device)