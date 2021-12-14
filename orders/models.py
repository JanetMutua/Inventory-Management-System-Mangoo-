from typing import FrozenSet
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.utils import timezone
from ItemGroups.models import ItemGroup
from suppliers.models import Supplier

# Create your models here.


class order(models.Model):
    supplier_name = models.ForeignKey(
        Supplier, on_delete=DO_NOTHING, null=True)
    deliver_to = models.TextField(null=True)
    order_date = models.DateTimeField(default=timezone.now)
    deliver_date = models.DateTimeField(null=True)
    payment_terms = models.CharField(max_length=100, null=True)
    item_group = models.ForeignKey(ItemGroup, on_delete=CASCADE, null=True)
    item_name = models.CharField(max_length=100, null=True)
    item_quantity = models.CharField(max_length=100, null=True)
    item_attribute = models.TextField(null=True)
