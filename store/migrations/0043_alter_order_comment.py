# Generated by Django 4.1.6 on 2023-03-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0042_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default=None, max_length=400, verbose_name='یادداشت سفارش'),
        ),
    ]
