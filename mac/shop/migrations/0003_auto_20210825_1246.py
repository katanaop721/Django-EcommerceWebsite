# Generated by Django 3.1.5 on 2021-08-25 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210825_1244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pro_name',
            new_name='product_name',
        ),
    ]
