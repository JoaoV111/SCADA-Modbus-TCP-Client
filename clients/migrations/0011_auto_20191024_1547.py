# Generated by Django 2.2.5 on 2019-10-24 18:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20191024_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 18, 47, 32, 574443, tzinfo=utc)),
        ),
    ]