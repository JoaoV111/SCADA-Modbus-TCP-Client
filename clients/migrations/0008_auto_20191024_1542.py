# Generated by Django 2.2.5 on 2019-10-24 18:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_auto_20191024_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 18, 42, 7, 796320, tzinfo=utc)),
        ),
    ]
