# Generated by Django 4.2.4 on 2023-08-16 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SparepartsApp', '0003_rename_item_name_product_part_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='part_number',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
