# Generated by Django 3.2.1 on 2022-10-23 14:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0016_alter_evidence_happened_oon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='happened_oon',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 14, 2, 27, 794036, tzinfo=utc)),
        ),
    ]
