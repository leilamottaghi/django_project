# Generated by Django 4.1.6 on 2023-02-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='user_email',
            field=models.EmailField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='address',
            name='user_name',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
