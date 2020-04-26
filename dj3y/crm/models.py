# the default import
from django.db import models

# my import
from django.db.models.functions import Concat
from django.db.models import Value
from django.urls import reverse
import uuid
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import timedelta

# my import which may grow during adding new models

# my code.


# a function using to get a default expire time
def get_default_expiration_time():
    return now() + timedelta(days=30)


# a abstract model of main models
class CrmBaseModel(models.Model):

    # the PK field
    id = models.AutoField(
        verbose_name='Serial Number',
        primary_key=True,
    )
    # the general fields
    code = models.CharField(
        verbose_name='Code',
        max_length=50,
        unique=True,
    )

    class Meta:
        abstract = True
        indexes = [models.Index(fields=['id'])]

    def get_absolute_url(self):
        return reverse(f'{self._meta.app_label}:{self._meta.model_name}_detail', args=[str(self.id)])

    def __str__(self):
        return self.code

    # this uses uuid.uuid4() to generate field 'code' automatically
    # doing this in clean() instead of in save() so that when getting duplicate value
    # the error message would show like a normal message on webpage
    # instead of a error exception leading crash.
    def clean(self):
        if self.code == '':
            self.code = f'{self._meta.verbose_name[0:3]}. {uuid.uuid4().hex[:6]}'
            if type(self).objects.filter(code=self.code).exists():
                raise ValidationError('You got a duplicate code, please save again.')


# a main model
class Person(CrmBaseModel):

    # the general fields
    name = models.CharField(
        verbose_name='Name',
        blank=True,
        max_length=100,
    )
    tax_id = models.CharField(
        verbose_name='Tax ID',
        blank=True,
        max_length=25,
    )
    phone_number = models.CharField(
        verbose_name='Phone Number',
        blank=True,
        max_length=25,
    )
    address = models.CharField(
        verbose_name='Address',
        blank=True,
        max_length=100,
    )
    registration_time = models.DateTimeField(
        verbose_name='Registration Time',
        blank=True,
        null=True,
    )
    expiration_time = models.DateTimeField(
        verbose_name='Expiration Time',
        blank=True,
        null=True,
    )
    remark = models.TextField(
        verbose_name='Remark',
        blank=True,
        max_length=400,
    )
    # the foreign key fields
    parent = models.ForeignKey(
        verbose_name='Parent',
        blank=True,
        null=True,
        to='Person',
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(model_name)s_parent_set',
    )
    # the many to many fields
    related_salesperson = models.ManyToManyField(
        verbose_name='Related Salespersons',
        blank=True,
        to='Person',
        symmetrical=False,
        related_name='%(app_label)s_%(model_name)s_related_salesperson_set',
    )

    class Meta(CrmBaseModel.Meta):
        verbose_name = 'Person'
        verbose_name_plural = 'People'
        ordering = [
            Concat(
                'name',
                Value(' ('),
                'code',
                Value(')'),
            ),
        ]

    # __str__() generated by combining code and name

    def __str__(self):
        if self.name == '':
            return self.code
        else:
            return f'{self.name} ({self.code})'
