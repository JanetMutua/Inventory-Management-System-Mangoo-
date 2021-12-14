from os import TMP_MAX
from django.db import models

# Create your models here.


class ItemGroup(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    units = models.CharField(max_length=100, null=True)
    attributes = models.TextField(null=True)
    tax = models.CharField(default='VAT', max_length=100, null=True)
