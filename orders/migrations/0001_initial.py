# Generated by Django 3.2 on 2021-12-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_name', models.CharField(max_length=100)),
                ('payment_terms', models.CharField(max_length=100)),
                ('item_group', models.CharField(max_length=100)),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.CharField(max_length=100)),
            ],
        ),
    ]
