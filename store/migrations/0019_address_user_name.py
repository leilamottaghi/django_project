# Generated by Django 4.1.6 on 2023-02-14 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_address_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='user_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
