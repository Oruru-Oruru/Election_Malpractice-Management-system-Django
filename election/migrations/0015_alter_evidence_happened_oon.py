# Generated by Django 3.2.1 on 2022-10-23 13:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0014_auto_20221023_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='happened_oon',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 13, 54, 29, 234419, tzinfo=utc)),
        ),
    ]