# Generated by Django 5.0.6 on 2024-08-21 16:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0004_delete_login_alter_register_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.TextField(max_length=50)),
                ('productquantity', models.IntegerField(default=0)),
                ('productprice', models.IntegerField(default=0)),
                ('productimage', models.ImageField(default='null.jpg', upload_to='proimage')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UserApp.register')),
            ],
        ),
    ]
