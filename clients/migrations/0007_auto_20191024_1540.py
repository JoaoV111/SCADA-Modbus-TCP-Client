# Generated by Django 2.2.5 on 2019-10-24 18:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_auto_20191024_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 18, 40, 30, 463388, tzinfo=utc)),
        ),
    ]