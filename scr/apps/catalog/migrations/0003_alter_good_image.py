# Generated by Django 5.1.3 on 2024-12-12 16:25

import apps.catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0002_good_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(
                default='default_good.svg', upload_to=apps.catalog.models.path_to_img
            ),
        ),
    ]
