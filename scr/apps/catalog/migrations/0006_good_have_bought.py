# Generated by Django 5.1.3 on 2024-12-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_remove_order_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='have_bought',
            field=models.IntegerField(default=0),
        ),
    ]
