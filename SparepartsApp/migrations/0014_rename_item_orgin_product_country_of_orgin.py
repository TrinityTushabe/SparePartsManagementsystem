# Generated by Django 4.2.4 on 2023-08-16 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SparepartsApp', '0013_product_part_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='item_orgin',
            new_name='country_of_orgin',
        ),
    ]
