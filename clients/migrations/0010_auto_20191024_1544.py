# Generated by Django 2.2.5 on 2019-10-24 18:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20191024_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 24, 18, 44, 53, 863518, tzinfo=utc)),
        ),
    ]