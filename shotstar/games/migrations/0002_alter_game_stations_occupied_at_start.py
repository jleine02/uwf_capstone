# Generated by Django 4.0.3 on 2022-03-04 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='stations_occupied_at_start',
            field=models.JSONField(default={1: False, 2: False, 3: False, 4: False, 5: False}),
        ),
    ]
