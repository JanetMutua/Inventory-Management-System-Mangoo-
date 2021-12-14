# Generated by Django 3.2 on 2021-12-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ItemGroups', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemgroups',
            name='unit',
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='attributes',
            field=models.TextField(default='foo'),
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='brand',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='manufacturer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='tax',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='itemgroups',
            name='units',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
