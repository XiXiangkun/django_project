# Generated by Django 2.1.7 on 2019-06-14 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAPP', '0009_auto_20190610_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='isSupervisor',
            field=models.IntegerField(default=0),
        ),
    ]
