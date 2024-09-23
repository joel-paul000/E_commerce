# Generated by Django 5.0.6 on 2024-08-21 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0005_remove_product_cateogoryname_product_category_id'),
        ('UserApp', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='productimage',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='productname',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='productprice',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='productquantity',
        ),
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AdminApp.product'),
        ),
    ]
