from django.db import models

# Create your models here.


class orders(models.Model):
    supplier_name = models.CharField(max_length=100)
    deliver_to = models.TextField
    order_date = models.DateTimeField
    deliver_date = models.DateTimeField
    payment_terms = models.CharField(max_length=100)
    item_group = models.CharField(max_length=100)
    item_name = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)
    item_attribute = models.TextField
