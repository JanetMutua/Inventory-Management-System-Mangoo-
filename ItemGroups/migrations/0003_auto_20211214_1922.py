# Generated by Django 3.2 on 2021-12-14 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ItemGroups', '0002_auto_20211214_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemgroups',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='itemgroups',
            name='manufacturer',
        ),
    ]
