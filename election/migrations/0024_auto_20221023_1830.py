# Generated by Django 3.2.1 on 2022-10-23 15:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0023_evidence_happened_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='evidence',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='election.category'),
        ),
        migrations.AddField(
            model_name='evidence',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='election.location'),
        ),
        migrations.AlterField(
            model_name='evidence',
            name='happened_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 23, 18, 30, 54, 56715)),
        ),
    ]
