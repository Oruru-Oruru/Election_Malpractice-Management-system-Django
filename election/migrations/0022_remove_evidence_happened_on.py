# Generated by Django 3.2.1 on 2022-10-23 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0021_alter_evidence_happened_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evidence',
            name='happened_on',
        ),
    ]