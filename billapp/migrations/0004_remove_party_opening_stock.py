# Generated by Django 3.2.24 on 2024-03-19 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0003_auto_20240318_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='party',
            name='opening_stock',
        ),
    ]
