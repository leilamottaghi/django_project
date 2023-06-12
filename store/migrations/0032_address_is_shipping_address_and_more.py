# Generated by Django 4.1.6 on 2023-03-04 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0031_remove_address_city_remove_address_user_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_shipping_address',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_link',
            field=models.URLField(default=None),
        ),
    ]
