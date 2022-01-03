from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from suppliers.models import Supplier
from ItemGroups.models import ItemGroup
# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=200, null=True)
    sku = models.IntegerField(null=True)
    unit_of_measure = models.CharField(default='unit_type', max_length=100)
    item_group = models.ForeignKey(ItemGroup, on_delete=CASCADE, null=True)
    purchase_price = models.CharField(max_length=100, null=True)
    cost_price = models.CharField(max_length=100, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=DO_NOTHING)
    manufacturer = models.CharField(max_length=100, null=True)
    brand = models.CharField(max_length=100, null=True)

    def unit_type():
        return 'Kg', 'Dozen', 'Pieces', 'Pairs'

    def __str__(self):
        return self.item_name
