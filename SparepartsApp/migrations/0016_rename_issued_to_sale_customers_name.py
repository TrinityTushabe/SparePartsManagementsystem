# Generated by Django 4.2.4 on 2023-08-16 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SparepartsApp', '0015_product_branch_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='issued_to',
            new_name='customers_name',
        ),
    ]
