# Generated by Django 5.0.6 on 2024-08-06 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cat',
            old_name='catname',
            new_name='cateogoryname',
        ),
        migrations.RenameField(
            model_name='pro',
            old_name='catname',
            new_name='cateogoryname',
        ),
        migrations.RenameField(
            model_name='pro',
            old_name='proimage',
            new_name='productimage',
        ),
        migrations.RenameField(
            model_name='pro',
            old_name='proname',
            new_name='productname',
        ),
    ]
