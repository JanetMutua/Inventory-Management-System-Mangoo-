from django.db import models

# Create your models here.


class Supplier(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    display_name = models.CharField(max_length=100)
    supplier_email = models.EmailField
    supplier_phone = models.IntegerField
    website = models.CharField(max_length=100)
    address = models.TextField
