# Generated by Django 3.2.1 on 2022-10-23 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0020_auto_20221023_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evidence',
            name='happened_on',
            field=models.DateTimeField(),
        ),
    ]
