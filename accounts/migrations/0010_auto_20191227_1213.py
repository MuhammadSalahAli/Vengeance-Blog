# Generated by Django 2.2.5 on 2019-12-27 12:13

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191226_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='/default/default.png', upload_to=accounts.models.save_profile_pic),
        ),
    ]
