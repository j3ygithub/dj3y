# the default import
from django.contrib import admin

# my import
from .models import Person

# my import which may grow during adding new models

# Register your models here.

admin.site.register(Person)