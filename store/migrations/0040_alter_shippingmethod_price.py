# Generated by Django 4.1.6 on 2023-03-09 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0039_shippingmethod_order_shipping_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingmethod',
            name='price',
            field=models.IntegerField(),
        ),
    ]
