# Generated by Django 2.2.5 on 2019-10-03 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_task'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': [('1', 'Tela Escritório'), ('2', 'Tela CNB')]},
        ),
    ]
