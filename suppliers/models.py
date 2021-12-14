from django.db import models

# Create your models here.


class Supplier(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    second_name = models.CharField(max_length=100, null=True)
    company_name = models.CharField(max_length=100, null=True)
    display_name = models.CharField(max_length=100, null=True)
    supplier_email = models.EmailField(null=True)
    supplier_phone = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
