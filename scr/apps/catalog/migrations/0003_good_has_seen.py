# Generated by Django 5.1.3 on 2024-12-10 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='has_seen',
            field=models.IntegerField(default=0),
        ),
    ]
