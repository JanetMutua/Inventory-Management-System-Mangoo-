# Generated by Django 3.2 on 2021-12-02 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('second_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
            ],
        ),
    ]