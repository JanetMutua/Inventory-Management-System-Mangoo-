from os import TMP_MAX
from django.db import models

# Create your models here.


class ItemGroups(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField
    unit = models.CharField(max_length=100)
    manufacturer = models.TextField
    brand = models.TextField
    attributes = models.TextField
    tax = models.TextField
